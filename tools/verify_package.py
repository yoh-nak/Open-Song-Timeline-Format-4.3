#!/usr/bin/env python3
"""OSTF 4.3.0 package integrity and static example-coverage inspection.

MIT license (LICENSE-CODE). Read-only. Never fetches URIs, invokes a plugin,
plays music or controls hardware. --coverage needs jsonschema.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
import warnings
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def strict_json(path):
    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ValueError('duplicate JSON key: ' + key)
            result[key] = value
        return result
    def number(text):
        value = float(text)
        if not math.isfinite(value) or (value == 0 and Decimal(text) != 0):
            raise ValueError('non-finite/underflowing JSON number: ' + text)
        return value
    def bad(text):
        raise ValueError('non-finite JSON constant: ' + text)
    value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                       parse_float=number, parse_constant=bad)
    def unicode_check(x):
        if isinstance(x,str): x.encode('utf-8', errors='strict')
        elif isinstance(x,dict):
            for k,v in x.items(): unicode_check(k); unicode_check(v)
        elif isinstance(x,list):
            for v in x: unicode_check(v)
    unicode_check(value)
    return value


def sha(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda:stream.read(1024*1024),b''):
            h.update(block)
    return h.hexdigest()


def inventory():
    result = {}
    for path in ROOT.rglob('*'):
        rel = path.relative_to(ROOT)
        if any(p in ('.git', '__pycache__') for p in rel.parts) or path.suffix == '.pyc':
            continue
        if path.is_symlink():
            raise ValueError('unexpected symlink: ' + str(rel))
        if path.is_file(): result[rel.as_posix()] = path
    return result


def verify_integrity():
    files = inventory()
    manifest = strict_json(ROOT/'PACKAGE_MANIFEST.json')
    if len(files) > 100 or len(files) != manifest['file_count']:
        raise ValueError('file-count limit or manifest count mismatch')
    records = manifest['files']
    names = [r['path'] for r in records]
    if len(names) != len(set(names)):
        raise ValueError('duplicate manifest path')
    expected = set(files)-{'PACKAGE_MANIFEST.json','SHA256SUMS.txt'}
    if set(names) != expected:
        raise ValueError('manifest inventory differs from the shipped files')
    for item in records:
        path = files[item['path']]
        if path.stat().st_size != item['bytes'] or sha(path) != item['sha256']:
            raise ValueError('manifest mismatch: '+item['path'])
    checks = {}
    for line in (ROOT/'SHA256SUMS.txt').read_text().splitlines():
        digest, name = line.split('  ',1)
        if name in checks or name not in files:
            raise ValueError('duplicate/unknown checksum path: '+name)
        checks[name] = digest
    if set(checks) != set(files)-{'SHA256SUMS.txt'}:
        raise ValueError('checksum inventory differs from the shipped files')
    for name,digest in checks.items():
        if sha(files[name]) != digest:
            raise ValueError('checksum mismatch: '+name)
    for name,path in files.items():
        if path.suffix in ('.json','.ostf'):
            strict_json(path)
    print(f'INTEGRITY: {len(files)} files; {len(records)} manifest records; {len(checks)} checksum records; exact matches')

class Coverage:
 def __init__(self, schema):
  self.schema=schema; self.resolver=RefResolver.from_schema(schema); self.validators={}
  self.properties={}; self.enums={}; self.branches={}; self.hits={}; self.enumhits={}; self.branchhits={}; self.reachable=set()
  self.collect(schema,'#',set())
 def resolve(self, ref):
  assert ref.startswith('#/')
  obj=self.schema
  for v in ref[2:].split('/'): obj=obj[v.replace('~1','/').replace('~0','~')]
  return obj
 def valid(self,s,v):
  key=id(s)
  if key not in self.validators:self.validators[key]=Draft202012Validator(s,resolver=self.resolver)
  return self.validators[key].is_valid(v)
 def collect(self,s,p,seen):
  if not isinstance(s,dict) or p in seen:return
  seen.add(p); self.reachable.add(p)
  if '$ref' in s: self.collect(self.resolve(s['$ref']),s['$ref'],seen)
  for k,sub in s.get('properties',{}).items():
   q=p+'/properties/'+k; self.properties[q]={'name':k,'schema':sub,'owner':p}; self.collect(sub,q,seen)
  if 'enum' in s:self.enums[p]=s['enum']
  for kw in ['items','additionalProperties','contains']:
   if isinstance(s.get(kw),dict): self.collect(s[kw],p+'/'+kw,seen)
  for k,sub in s.get('patternProperties',{}).items(): self.collect(sub,p+'/patternProperties/'+k,seen)
  for kw in ['oneOf','anyOf','allOf']:
   for i,sub in enumerate(s.get(kw,[])):
    q=p+f'/{kw}/{i}'
    if kw in ('oneOf','anyOf'):self.branches[q]=sub
    self.collect(sub,q,seen)
  # Predicate properties are not parameter declarations. Then/else often only restrict fields already declared.
  for kw in ['then','else']:
   if kw in s:self.collect(s[kw],p+'/'+kw,seen)
 def walk(self,s,p,v,ptr,file,stack=None):
  if not isinstance(s,dict):return
  if stack is None:stack=set()
  guard=(p,ptr)
  if guard in stack:return
  stack=stack|{guard}
  if '$ref' in s:self.walk(self.resolve(s['$ref']),s['$ref'],v,ptr,file,stack)
  if 'enum' in s and v in s['enum']:
   self.enumhits.setdefault(p,{})[json.dumps(v,ensure_ascii=False)]=(file,ptr)
  if isinstance(v,dict):
   for k,sub in s.get('properties',{}).items():
    if k in v:
     q=p+'/properties/'+k
     self.hits.setdefault(q,[])
     if len(self.hits[q])<3:self.hits[q].append((file,ptr+'/'+k))
     self.walk(sub,q,v[k],ptr+'/'+k,file,stack)
   import re
   for k,val in v.items():
    matches=[]
    for pat,sub in s.get('patternProperties',{}).items():
     if re.search(pat,k): matches.append(pat); self.walk(sub,p+'/patternProperties/'+pat,val,ptr+'/'+k,file,stack)
    if k not in s.get('properties',{}) and not matches and isinstance(s.get('additionalProperties'),dict):self.walk(s['additionalProperties'],p+'/additionalProperties',val,ptr+'/'+k,file,stack)
  if isinstance(v,list) and isinstance(s.get('items'),dict):
   for i,val in enumerate(v):self.walk(s['items'],p+'/items',val,ptr+'/'+str(i),file,stack)
  for kw in ['oneOf','anyOf','allOf']:
   for i,sub in enumerate(s.get(kw,[])):
    if kw=='allOf' or self.valid(sub,v):
     q=p+f'/{kw}/{i}'
     if kw!='allOf':self.branchhits.setdefault(q,(file,ptr))
     self.walk(sub,q,v,ptr,file,stack)
  if 'if' in s:
   kw='then' if self.valid(s['if'],v) else 'else'
   if kw in s:self.walk(s[kw],p+'/'+kw,v,ptr,file,stack)
 def add(self,data,file): self.walk(self.schema,'#',data,'',file)
 def summary(self):
  missing=[p for p in self.properties if p not in self.hits]
  enums=[(p,[v for v in vs if json.dumps(v,ensure_ascii=False) not in self.enumhits.get(p,{})]) for p,vs in self.enums.items()]
  return {'properties':len(self.properties),'covered':len(self.properties)-len(missing),'missing':missing,'enum_values':sum(map(len,self.enums.values())),'missing_enums':[(p,v) for p,v in enums if v], 'branches':len(self.branches),'missing_branches':[p for p in self.branches if p not in self.branchhits]}


def verify_coverage():
    global Draft202012Validator, RefResolver
    try:
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', DeprecationWarning)
            from jsonschema import Draft202012Validator, RefResolver, FormatChecker
    except ImportError as exc:
        raise ValueError('coverage mode requires: python -m pip install -r requirements.txt') from exc
    report = strict_json(ROOT/'docs'/'COVERAGE_REPORT.json')
    totals = [0,0,0]
    for family,record in report['families'].items():
        schema_path=ROOT/record['schema']
        if sha(schema_path)!=record['schema_sha256']:
            raise ValueError('coverage schema fingerprint changed: '+family)
        schema=strict_json(schema_path)
        validator=Draft202012Validator(schema,format_checker=FormatChecker())
        coverage=Coverage(schema)
        for name in record['sample_files']:
            path=ROOT/name
            if not path.resolve().is_relative_to(ROOT.resolve()):
                raise ValueError('sample path escapes repository')
            data=strict_json(path)
            errors=list(validator.iter_errors(data))
            if errors:
                raise ValueError(name+': '+errors[0].message)
            coverage.add(data,name)
        summary=coverage.summary()
        if summary['missing'] or summary['missing_enums'] or summary['missing_branches']:
            raise ValueError('coverage is incomplete: '+family)
        count=record['counts']
        metrics=[summary['properties'],summary['enum_values'],summary['branches']]
        expected=[count['parameter_declarations'],count['enumerated_values'],count['positive_union_branches']]
        if metrics!=expected:
            raise ValueError('coverage count drift: '+family)
        if set(coverage.properties)!={r['schema_pointer'] for r in record['parameters']}:
            raise ValueError('coverage field list drift: '+family)
        for item in record['parameters']:
            witnesses={(f,p) for f,p in coverage.hits[item['schema_pointer']]}
            if any((w['file'],w['json_pointer']) not in witnesses for w in item['witnesses']):
                raise ValueError('stored field witness drift: '+item['schema_pointer'])
        totals=[a+b for a,b in zip(totals,metrics)]
        print(f'COVERAGE {family}: {metrics[0]} parameter declarations; {metrics[1]} enum literals; {metrics[2]} positive union branches')
    print(f'TOTAL COVERAGE: {totals[0]} / {totals[1]} / {totals[2]}')
    print('Static content coverage only; not independent semantic, runtime, DAW, plugin, voice, WAN or hardware certification.')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--coverage',action='store_true',help='Also re-parse examples and reproduce schema-defined coverage (requires jsonschema)')
    args=parser.parse_args()
    try:
        verify_integrity()
        if args.coverage:verify_coverage()
        return 0
    except Exception as exc:
        print('CHECK FAILED:',str(exc),file=sys.stderr)
        return 1

if __name__=='__main__':
    sys.exit(main())

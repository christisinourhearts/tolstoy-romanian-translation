#!/usr/bin/env python3
"""Validate Romanian translations against the audited Russian source.

usage: validate_translation.py /path/to/tolstoy-russian-md

Adapted from tolstoy-english-translation/project/tools/validate_translation.py,
with Romanian-specific checks (comma-below diacritics).
"""
import sys, json, pathlib, re, hashlib

if len(sys.argv) != 2:
    raise SystemExit('usage: validate_translation.py /path/to/tolstoy-russian-md')
ru = pathlib.Path(sys.argv[1])
ro = pathlib.Path(__file__).resolve().parents[2]
rows = [json.loads(x) for x in (ro / 'project' / 'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]

page_re = re.compile(r'<!--\s*vol\.\s*\d+,\s*p\.\s*[^>]+?-->')
fn_ref_re = re.compile(r'\[\^([^\]]+)\](?!:)')
fn_def_re = re.compile(r'^\[\^([^\]]+)\]:', re.M)
front_re = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.S)


def yaml_scalar(text, key):
    m = re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$', text)
    return m.group(1).strip() if m else None


errors, warnings, checked = [], [], 0
seen_paths, seen_ids = set(), set()
for r in rows:
    op = r['output_path']
    if op in seen_paths: errors.append((op, 'duplicate output path'))
    if r['id'] in seen_ids: errors.append((op, 'duplicate stable id'))
    seen_paths.add(op); seen_ids.add(r['id'])
    if r.get('translation_status') == 'reviewed':
        for k in ('fidelity_audit_status', 'final_source_audit_status'):
            if r.get(k) not in ('pass', 'passed'): errors.append((op, f'reviewed but {k} is not pass'))
        if r.get('romanian_edit_status') != 'complete': errors.append((op, 'reviewed but Romanian edit is not complete'))
        if r.get('coverage_audit_status') != 'pass': errors.append((op, 'reviewed but coverage audit has not passed'))
        cov = ro / 'project' / 'qa' / 'coverage' / (r['source_ru_path'].replace('/', '__')[:-3] + '.json')
        if not cov.exists(): errors.append((op, f'missing coverage record {cov.name}'))
    tp = ro / op
    if not tp.exists():
        if r.get('translation_status') == 'reviewed': errors.append((op, 'reviewed row missing Romanian file'))
        continue
    rp = ru / r['source_ru_path']
    if not rp.exists(): errors.append((op, 'missing Russian source')); continue
    if hashlib.sha256(rp.read_bytes()).hexdigest() != r['source_ru_sha256']:
        errors.append((op, 'Russian source checksum changed'))
    rt = rp.read_text(encoding='utf-8'); tt = tp.read_text(encoding='utf-8')
    if page_re.findall(rt) != page_re.findall(tt): errors.append((op, 'page-marker sequence differs'))
    if rt.count('~~') != tt.count('~~'): errors.append((op, 'deletion-markup delimiter count differs'))
    fm = front_re.match(tt)
    if not fm: errors.append((op, 'missing YAML front matter'))
    else:
        f = fm.group(1)
        if yaml_scalar(f, 'source_ru_path') != r['source_ru_path']: errors.append((op, 'front-matter source_ru_path mismatch'))
        if yaml_scalar(f, 'source_ru_sha256') != r['source_ru_sha256']: errors.append((op, 'front-matter source_ru_sha256 mismatch'))
    sdefs = set(fn_def_re.findall(rt)); tdefs = set(fn_def_re.findall(tt)); trefs = set(fn_ref_re.findall(tt))
    if trefs - tdefs: errors.append((op, f'dangling footnote refs: {sorted(trefs - tdefs)[:10]}'))
    if r.get('apparatus_translation_status') in ('translated', 'complete', 'not_applicable') and sdefs != tdefs:
        errors.append((op, f'footnote ids differ source={sorted(sdefs)} target={sorted(tdefs)}'))
    body = front_re.sub('', tt, count=1)
    if re.search(r'[şţŞŢ]', body): errors.append((op, 'cedilla ş/ţ found; use comma-below ș/ț'))
    if re.search(r'[А-Яа-яЁё]', body): warnings.append((op, 'Cyrillic remains in Romanian body; verify intentional'))
    checked += 1

print(f'Romanian files checked: {checked:,}')
print(f'errors: {len(errors):,}')
print(f'warnings: {len(warnings):,}')
for p, m in errors[:100]: print('ERROR', p, m)
for p, m in warnings[:50]: print('WARNING', p, m)
raise SystemExit(1 if errors else 0)

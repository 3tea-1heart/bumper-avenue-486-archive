"""Verify every retained source file and the actual message count."""
from pathlib import Path
import hashlib, json

root = Path(__file__).resolve().parents[1]
verified = 0
for line in (root / 'SOURCE_SHA256.txt').read_text('utf-8').splitlines():
    digest, name = line.split('  ', 1)
    actual = hashlib.sha256((root / name).read_bytes()).hexdigest()
    if actual != digest: raise SystemExit('Checksum mismatch: ' + name)
    verified += 1
manifest = json.loads((root / 'data/manifest.json').read_text('utf-8'))
count = 0
ids = set()
for part in manifest['chunks']:
    raw = (root / part['file']).read_text('utf-8')
    messages = json.loads(raw[raw.index('messages:') + 9:raw.rfind(']') + 1])
    assert len(messages) == part['count'], part['id']
    count += len(messages)
    ids.update(m['id'] for m in messages)
assert count == manifest['stats']['totalMessages']
assert len(ids) == count, 'Duplicate message IDs'
for file in root.rglob('*'):
    if file.is_file() and '.git' not in file.parts:
        assert file.stat().st_size < 100 * 1024 * 1024, 'GitHub file limit: ' + file.name
print(f'PASS: {verified} original files, {count} messages, {len(manifest["chunks"])} chunks; unique IDs; no file >= 100 MiB.')

"""Read-only project checks; no network, git mutations, or medical validation.

Run from any directory. --empty also checks the initial empty data layers.
--privacy enables the heuristic publication scan.
"""
import argparse
import ast
import hashlib
import json
from pathlib import Path
import re
import sys
import materials

ROOT = Path(__file__).resolve().parents[1]
LAYERS = ('incoming', 'raw', 'materials', 'records', 'overview', 'outputs',
          'scripts', 'documentation', 'temp', 'examples')
DATA_LAYERS = {'incoming', 'raw', 'materials', 'records', 'overview', 'outputs'}
# LF-normalized baselines of the reviewed, empty working layers.
STARTER = {
    'incoming/AGENTS.md': '29013b196939ac3bc6adf32407d75ba33bbd88a47a2aaff6d6d70ab69f50f92f',
    'raw/AGENTS.md': '0e019ce0090966c5764439f047355b438a94bef6c12e1ab6d06e7325444bf693',
    'raw/undated/AGENTS.md': '5001dc802d8781e924904202b6d7113aafd02e5439ae4f685068750013a046bd',
    'materials/AGENTS.md': '0e28ffac6254d8104620ef46d1b7b37c79f28866aaf91fc75174012e64a1e0a9',
    'materials/classification.json': 'd39f8773a870608a40458cd335452769d7d4f1130a2c56ac6a7d71a6bc3c29c0',
    'materials/INDEX.md': '299dd2cd9253fdc7b2db4eff29dee3ba7fd90ba881f206a8a16079030e7c88d4',
    'materials/manifest.json': '0e95acfa9bd51fe04f4cfab7ebf2fb5454c9b6fe3a720262a3f5a3dd6b890a65',
    'materials/undated/AGENTS.md': '58dcd396e65316965532fa5781442ce96226d6a448d3d9d6517fe8930e0b9b63',
    'records/AGENTS.md': '721a399560d09ab8880bf105b84723cb1d881f82ad63b99d1943206244f454e8',
    'records/DATABASE.md': '4c11d9087787079cba861e1b2b4c618b732cbbd29c41ed44f4a9d77e2a1681fd',
    'records/INDEX.md': '89242506890a0b1983fb8cd0639128063c77df226824d50812b9885c3416fb56',
    'records/measurements/AGENTS.md': 'e2cdc27ccf6d9c8125c9e5d8440b6f4c2efa952a8280a4e0ab9702691bd54311',
    'records/medications/AGENTS.md': '47a0e0c20d64ee44aa9f294ad8c367066c986fc93fb8662aa5a01becce808309',
    'records/medications/CURRENT.md': 'd929eaf71ec03ea93553e500f1d3272ad75ed2d85fc0853c024407db83ad1bfe',
    'records/topics/AGENTS.md': 'c5f2e86fc34c3e8575e173f91d9f6de099a23db7e08bd2b9b46bb054f769d49f',
    'overview/AGENTS.md': 'bd572d888f412cba587731dee08196aadb26d485a7a7d34ab460097e52c43b58',
    'outputs/AGENTS.md': '95101ea44db4639db2215a205fe07b347dd16ae48e6108fbda859fd04e2dfb5c',
}

def documents():
    for path in sorted(ROOT.rglob('*')):
        parts = path.relative_to(ROOT).parts
        if path.is_file() and not any(x in parts for x in ('.git', '.venv', 'venv', '__pycache__', 'temp')):
            yield path

def anchors(text):
    text = materials.markdown_prose(text)
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen = {}
    for heading in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        slug = re.sub(r'[^\w\s-]', '', heading.lower()).replace(' ', '-')
        count = seen.get(slug, 0)
        seen[slug] = count + 1
        result.add(slug + ('-' + str(count) if count else ''))
    return result


def empty_layer_errors():
    errors = []
    # Enumerate the working layers directly, including normally ignored folders.
    for layer in sorted(DATA_LAYERS):
        for path in (ROOT / layer).rglob('*'):
            rel = path.relative_to(ROOT).as_posix()
            if path.is_symlink() or (path.is_file() and rel not in STARTER):
                errors.append('Unexpected private-layer file: ' + rel)
    for name, expected in STARTER.items():
        try:
            text = (ROOT / name).read_text(encoding='utf-8')
            if hashlib.sha256(text.encode('utf-8')).hexdigest() != expected:
                errors.append('Starter content changed: ' + name)
        except (OSError, UnicodeError):
            errors.append('Missing or unreadable starter file: ' + name)
    return errors


def verify(empty=False, *, privacy=False):
    errors = []
    for folder in LAYERS:
        if not (ROOT / folder / 'AGENTS.md').is_file():
            errors.append('Missing layer rules: ' + folder)
    required = ['AGENTS.md', 'README.md', '.gitignore', 'requirements.txt',
                'documentation/ARCHITECTURE.md', 'documentation/CURRENT.md',
                'documentation/DECISIONS.md', 'documentation/REQUIREMENTS.md',
                'documentation/PRIVACY.md', 'documentation/CHECKS.md', '.gitattributes']
    for name in required:
        if not (ROOT / name).is_file():
            errors.append('Missing required file: ' + name)
    files = list(documents())
    for path in files:
        name = path.relative_to(ROOT).as_posix()
        if privacy and (path.name == '.env' or path.name.startswith('.env.')):
            errors.append(name + ': review local environment file before publication')
        if path.suffix not in ('.md', '.py', '.json', '.jsonl', '.txt', '.sql'):
            continue
        try:
            text = path.read_text(encoding='utf-8-sig')
            if path.suffix == '.py':
                ast.parse(text, filename=name)
            if path.suffix == '.json':
                json.loads(text)
            if path.suffix == '.jsonl':
                for line in text.splitlines():
                    if line.strip():
                        json.loads(line)
            if path.suffix == '.md':
                for target in materials.markdown_links(text):
                    location = materials.link_target(target)
                    if location is None:
                        continue
                    destination, fragment = location
                    linked = (path.parent / destination).resolve() if destination else path
                    if not linked.is_relative_to(ROOT) or not linked.exists():
                        errors.append(f'{name}: missing/outside link {target}')
                    elif fragment and linked.suffix == '.md':
                        if fragment not in anchors(linked.read_text(encoding='utf-8-sig')):
                            errors.append(f'{name}: missing anchor {target}')
            # Flag user-machine paths and common contact/secret formats, not values.
            patterns = (r'(?i)[a-z]:[\\/](?:users|work)[\\/]',
                        r'(?i)/(?:users|home)/[^/\s]+/',
                        r'[\w.+-]+@[\w.-]+\.[a-zA-Z]{2,}',
                        r'\+(?:375|7|380)\s*\(?\d[\d() -]{8,}',
                        r'(?i)(?:sk-[a-z0-9]{20,}|ghp_[a-z0-9]{20,})')
            if privacy and any(re.search(pattern, text) for pattern in patterns):
                errors.append(name + ': possible personal path/contact/secret; review required')
        except (ValueError, SyntaxError, OSError) as error:
            errors.append(f'{name}: {error}')
    if empty:
        errors.extend(empty_layer_errors())
    if errors:
        raise ValueError('\n'.join(errors))
    print('PASS: project structure, local links/anchors, JSON and Python syntax.'
          + (' Empty data layers checked.' if empty else '')
          + (' Heuristic privacy scan passed.' if privacy else ''))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--empty', action='store_true')
    parser.add_argument('--privacy', action='store_true', help='Scan for personal paths, contacts and secrets')
    try:
        args = parser.parse_args()
        verify(args.empty, privacy=args.privacy)
    except (ValueError, OSError) as error:
        print('ERROR: ' + str(error), file=sys.stderr)
        sys.exit(1)

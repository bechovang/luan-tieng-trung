import re
import os

# Paths to your files
BIB_FILE = 'ref/refs.bib'
TEX_DIR = '.'  # Current directory

# Extract all keys from .bib file
with open(BIB_FILE, encoding='utf-8') as f:
    bib_content = f.read()
bib_keys = set(re.findall(r'@\w+\{([^,]+),', bib_content))

# Find all .tex files
tex_files = []
for root, dirs, files in os.walk(TEX_DIR):
    for file in files:
        if file.endswith('.tex'):
            tex_files.append(os.path.join(root, file))

# Extract citation keys from all .tex files
all_tex_keys = set()
for tex_file in tex_files:
    try:
        with open(tex_file, encoding='utf-8') as f:
            tex_content = f.read()
        # Find all \footcite{key} and \footcite{key1}\footcite{key2}...
        tex_keys = re.findall(r'\\footcite\{([^}]+)\}', tex_content)
        # If there are multiple keys in one \footcite, split them
        for group in tex_keys:
            for key in group.split(','):
                all_tex_keys.add(key.strip())
        print(f"Checked: {tex_file}")
    except Exception as e:
        print(f"Error reading {tex_file}: {e}")

# Find missing keys
missing = all_tex_keys - bib_keys

print("\n" + "="*50)
print("MISSING CITATION KEYS IN refs.bib:")
print("="*50)
if missing:
    for key in sorted(missing):
        print(f"  - {key}")
else:
    print("  No missing keys found!")
print("="*50)

print(f"\nSummary:")
print(f"  - Total citation keys found in .tex files: {len(all_tex_keys)}")
print(f"  - Total keys in refs.bib: {len(bib_keys)}")
print(f"  - Missing keys: {len(missing)}")
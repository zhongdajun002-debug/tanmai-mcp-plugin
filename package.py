"""Build one portable plugin archive from the marketplace source."""
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

root = Path(__file__).resolve().parent
plugin = root / 'plugins' / 'tanmai'
manifest = json.loads((plugin / 'plugin.json').read_text())
output = root / 'dist' / ('tanmai-' + manifest['version'] + '.zip')
output.parent.mkdir(exist_ok=True)
with ZipFile(output, 'w', ZIP_DEFLATED) as archive:
    for path in sorted(plugin.rglob('*')):
        if path.is_file():
            archive.write(path, Path('tanmai') / path.relative_to(plugin))
print(output)

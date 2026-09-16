"""Bundle the offline app as a single HTML file. Python 3, standard library only."""
from pathlib import Path
root = Path(__file__).resolve().parent
src = root / 'dist'
html = (src / 'index.html').read_text(encoding='utf-8')
html = html.replace('<link rel="stylesheet" href="style.css">', '<style>' + (src / 'style.css').read_text(encoding='utf-8') + '</style>')
for name in ['vendor/jszip.min.js', 'core.js', 'xlsx-reader.js', 'app.js']:
    script = (src / name).read_text(encoding='utf-8').replace('</script', '<\\/script')
    html = html.replace(f'<script src="{name}"></script>', '<script>' + script + '</script>')
(root / 'Ilmastovisio.html').write_text(html, encoding='utf-8')
print('Ilmastovisio.html built successfully.')

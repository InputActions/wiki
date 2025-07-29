project = 'InputActions'
copyright = '2025, taj_ny'
author = 'taj_ny'
release = 'v0.8.0'

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design"
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

master_doc = 'index'

source_suffix = {
    '.md': 'markdown'
}

myst_enable_extensions = [
    'colon_fence',
    'strikethrough'
]
myst_heading_anchors = 6

html_css_files = ['styles.css']
html_title = 'InputActions v0.8.0'
html_theme = 'furo'
html_static_path = ['_static']

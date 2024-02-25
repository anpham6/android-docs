# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'squared'
copyright = 'squared 2024'
author = 'An Pham'
release = '5.1.5'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

primary_domain = 'js'
highlight_language = 'javascript'
pygments_style = 'abap'

nitpick_ignore = [
  ('js:func', 'string'),
  ('js:func', 'number'),
  ('js:func', 'boolean'),
  ('js:func', 'function'),
  ('js:func', 'object'),
  ('js:func', 'array'),
]

rst_prolog = """
.. role:: alt(emphasis)
.. role:: target(emphasis)
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_theme_options = {
  'style_nav_header_background': 'url(https://squared.readthedocs.io/en/latest/_static/places/001.png)',
  'navigation_depth': 3,
  'includehidden': False,
}
html_static_path = ['_static']
html_css_files = ['role.css', 'content.css', 'highlight-abap.css', 'override.css']
html_context = {
  'display_github': False,
  'commit': False,
}
html_show_copyright = False
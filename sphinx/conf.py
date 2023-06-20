## import os
## import sys
## sys.path.insert(0, os.path.abspath("_themes"))
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'German Emigration Records'
copyright = '2023, Kurt Krueckeberg'
author = 'Kurt Krueckeberg'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['myst_parser']

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'readme.md']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'material_theme'

html_theme_options = {
   'base_url': 'http://kurt-krueckeberg.io/',
   'repo_url': 'https://github.com/kurt-krueckeberg/kurt-krueckeberg.github.io/',
   'html_minify': True,
   'css_minify': True,
   'logo_icon': '&#xe869',
   'globaltoc_depth': 2
}

html_static_path = ['_static']

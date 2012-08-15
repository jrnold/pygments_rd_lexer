from setuptools import setup
entry_points = """
[pygments.lexers]
   bugs = pygments_lexer_rd:RdLexer
"""

setup(
    name = "pygments_lexer_rd",
    version = "0.1",
    py_modules = ['pygments_lexer_rd'],
    install_requires = ['pygments >= 1.4'],
    # Metadata
    author = "Jeffrey B. Arnold",
    description = "Pygments lexers for R documentation (Rd) files",
    license = "BSD",
    entry_points = entry_points
)

# -*- coding: utf-8 -*-
""" Pygments lexer for R documentation (Rd) files

    :copyright: Copyright 2012 Jeffrey B. Arnold
    :license: BSD, see LICENSE for details.
"""
from pygments.lexer import RegexLexer
from pygments.token import Comment, Punctuation, Keyword, String, Text

__all__ = ['RdLexer']

class RdLexer(RegexLexer):
    """ Pygments Lexer for R documentation (Rd) files

    This is a very minimal implementation, highlighting little more
    than the macros. A description of Rd syntax is found in `Writing R
    Extensions <http://cran.r-project.org/doc/manuals/R-exts.html>`_
    and `Parsing Rd files <developer.r-project.org/parseRd.pdf>`_.

    """
    name = 'Rd'
    aliases = ['rd']
    filenames = ['*.Rd']

    tokens = {
        'root' : [
            # catch escaped brackets and percent sign
            (r'\\[{}%]', String.Escape),
            # comments
            (r'%.*$', Comment),
            # special macros with no arguments
            (r'\\(?:cr|l?dots|R|tab)\b', Keyword.Constant),
            # macros
            # TODO: split into real macros names with sections and markup macros.
            (r'\\[a-zA-Z]+\b', Keyword),
            # special preprocessor macros
            (r'^#(?:ifn?def|endif).*\b', Comment.Preproc),
            # Non escaped brackets
            (r'[{}\[\]]', Punctuation),
            # everything else
            (r'.', Text),
            ]
        }



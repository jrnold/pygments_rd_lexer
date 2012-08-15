# -*- coding: utf-8 -*-
""" Pygments lexer for Rd files

    :copyright: Copyright 2012 Jeffrey B. Arnold
    :license: BSD, see LICENSE for details.
"""
from pygments.lexer import RegexLexer, include, bygroups, using
from pygments.lexers.math import SLexer
from pygments.token import Comment, Punctuation, Keyword, Name, \
     Operator, Number, Text, String

class RdLexer(RegexLexer):
    """
    Lexer for the Rd (R documentation) format
    """

    name = 'Rd'
    aliases = ['rd']
    filenames = ['*.Rd']

    # macros with no arguments
    CONSTANTS = ['cr', 'dots', 'ldots', 'R', 'tab']

    # Macros with R text
    RLIKE = ['code', 'dontshow', 'donttest', 'testonly',
             'examples', 'usage']
    # Verbatim and 1 argument
    VERBATIM1 = ['dontrun', 'env', 'kbd', 'option',
                 'out', 'preformatted', 'samp', 'special',
                 'url', 'verb', 'deqn', 'eqn',
                 'alias', 'Rdversion', 'synopsis', 'RdOpts', 'Sexpr', 
                 'href' # 2nd arg of href will be formatted normally
                 ]
    # Verbatim and 2 arguments
    VERBATIM2 = ['newcommand', 'renewcommand', 'deqn', 'eqn']
    # Can be included in strings in R-like text
    SPECIAL = ['link', 'var']

    tokens = {
        'brackets': [
            (r'(?<!\\)\{', String, '#push')
            (r'(?<!\\)\}', String, '#pop')
            ],
        'comment': [
            (r'%.*?\n', Comment.Single),  
            ],
        'macro':[
            (r'\\([a-zA-Z]+\b)', Keyword),            
            ],
        'string_macros':[
            (r'\\%s\b)' % r'|'.join(SPECIAL), Keyword),
            ],
        # latexlike
        'root': [
            # Pre-processor
            (r'^\#(ifn?def|endif).*$', Comment.Preproc, 'preproc'),
            # Other macros
            (r'[{}]', Operator),
            (r'.', Text)
        ],
        'options': [
            ],
        'verbatim': [
            include('comment')
            include('brackets')
            (r'.', String)
            ],
        'rlike': [
            include('comment')
            include('macro')
            (r'\'', String, 'string_squote'),
            (r'\"', String, 'string_dquote'),
            include('brackets')
            (r'.', String)
            ],
        'string_squote': [
            (r'[^\']*\'', String, '#pop'),
        ],
        'string_dquote': [
            (r'[^\"]*\"', String, '#pop'),
        ],

    }


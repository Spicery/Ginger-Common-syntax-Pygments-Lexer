# -*- coding: utf-8 -*-
"""
Setup for the Ginger Common syntax Pygments Lexer
"""
from setuptools import setup
 
__author__ = 'Stephen Leach <stephen.leach@steelypip.com>'

__doc__ = """\
A Ginger Common synyax lexer for Pygments as a separately-installable
package.
"""

setup(
    name='Ginger Common syntax Pygments Lexer',
    version='0.1.0',
    description=__doc__,
    author=__author__,
    packages=['common_lexer'],
    entry_points='''[pygments.lexers]
commonlexer = common_lexer:CommonLexer
'''
)
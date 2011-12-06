Ginger Common Syntax Lexer for Pygments
=======================================

This is a [pygments](http://pygments.org/) lexer for the [Ginger](http://github.com/Spicery/ginger) Common syntax.

Example
-------

    define nfib( n ) =>>
        if n <= 1 then
            1
        else
            1 + nfib( n - 1 ) + nfib( n - 2 )
        endif
    enddefine;

Installing
----------

    sudo python setup.py install

Development code
----------------

    pip install -e git+git://github.com/Spicery/Ginger-Common-syntax-Pygments-Lexer.git#egg=Ginger-Common-syntax-Pygments-Lexer

Syntax highlighting examples
----------------------------

    pygmentize sample.common


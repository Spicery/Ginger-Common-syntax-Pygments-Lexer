SPARQL Syntax Lexer for Pygments
================================

This is a [pygments](http://pygments.org/) lexer for [SPARQL](http://en.wikipedia.org/wiki/SPARQL), the semantic web query language.

Example
-------

    PREFIX owl:  <http://www.w3.org/2002/07/owl#> 

    SELECT DISTINCT ?class 
    FROM <http://www.w3.org/2002/07/owl#>
    WHERE { ?thing a ?class }

Installing
----------

    sudo python setup.py install

Development code
----------------

    pip install -e git+git://github.com/gjhiggins/sparql_pygments_lexer.git#egg=SPARQL_Pygments_Lexer

Syntax highlighting examples
----------------------------

    pygmentize example.sparql


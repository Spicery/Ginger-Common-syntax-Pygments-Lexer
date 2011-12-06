# -*- coding: utf-8 -*-
#!/usr/bin/env python

# from pygments.lexer import bygroups
# from pygments.lexer import include
# from pygments import highlight
from pygments.lexer import RegexLexer
from pygments.token import Comment
from pygments.token import Keyword
from pygments.token import Literal
from pygments.token import Name
from pygments.token import Number
from pygments.token import Operator
from pygments.token import Punctuation
from pygments.token import Text
from pygments.token import Token

__all__ = ['CommonLexer']

class CommonLexer(RegexLexer):
    name = u'Common'
    aliases = [u'common']
    filenames = ['*.common']

    tokens = {
        'root': [
            # There are a couple of other non-coding constructs, including long
            # comments that I will want to sort out later.
            (r'#[- #].*$', Comment),                                                  # End of line comments.
            
            # Legitimate whitespace - nothing special.
            (r'\s+', Text),                                                                   # Whitespace.
            
            # This is a complete list of the reserved words of Common.
            (r'case|catch|define|do|else|elseif|elseunless|enddefine|endfn|endfor|endif|endpackage|endswitch|endtransaction|endtry|endunless|fn|for|from|if|import|in|package|return|switch|then|throw|to|transaction|try|unless|until|val|var|while|with', Token.Keyword.Reserved ),

            # This is an incomplete definition of names, mainly because the
            # ASCII escape syntax is not properly defined.
            (r'[a-zA-Z_]\w*', Name),                                                                  # Keywords.
            
            # This is not right either, since we support floating point (in principle).
            (r'[-+]?\d+', Number),                                                                    # Numbers.
            
            # This is correct. Brackets may be decorated by repeated %s.
            (r'[\(\[\{]%*', Punctuation),                                             # Punctuation.
            (r'%*[\)\]\}]', Punctuation),                                             # Punctuation.
            # Special case. Needs more work (as does the syntax).
            (r'\$\{', Punctuation),
            
            # Commas and semicolons have very limited glueing power. Similarly 
            # the . and @ operator to prevent catastrophic typos.
            (r',+', Text),                                                                    # Self-glue.
            (r';+', Text),                                                                    # Self-glue.
            (r'\.+', Operator),                                                                       # Self-glue.
            (r'\@+', Operator),                                                                       # Self-glue.
            (r'\*+', Operator),                                                                       # Self-glue.
            
            # This is a very poor definition of strings and symbols. Really should
            # work on capturing interpolations with Token.Literal.String.Interp
            (r'"[^"]*"', Literal.String.Double ),                                     # String
            (r"'[^']*'", Literal.String.Single ),                                     # Symbol
            
            # There are three special constants. Arguably "present" should be added
            # but I am not keen on that name. Even "absent" bothers me to be honest.
            (r'absent|true|false', Keyword.Constant),                               # Reserved Word.
            
            # The boolean operators are special - and this is because they are 
            # likely to become incorporated into the sophisticated Prolog-like
            # extension of the language. In this extension the 'if' syntax is 
            # interpreted as 'if QUERY then' and it succeeds if there is a solution
            # to the QUERY.
            (r'and|or|not', Operator.Word ),                                  # Operator.
            
            # Sign characters all glue with one exception, a > may not be followed 
            # by <. This restriction is necessary for writing expression like this:
            #       <li> "Some text" </li><li> "More text" </li>
            # In this definition we use negative lookbehind (?<! to capture that.
            (r'[-+|/!?@$%^:=><](?:[-+|/!?@$%^:=>]|(?<!>)<)*', Operator )
        ]
    }

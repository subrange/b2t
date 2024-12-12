import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lexer import Lexer

def test_lexer():
    statements = """
    10 LET X = 10
    20 LET Y = 5
    30 PRINT X + Y
    40 IF X > Y THEN PRINT "X is greater" ELSE PRINT "Y is greater"
    50 REM This is a comment
    60 GOTO 10
    70 END
    """.strip()
    lexer=Lexer(statements)
    tokens=[]
    t=lexer.next_token()
    while t.typ!='EOF':
        tokens.append(t)
        t=lexer.next_token()

    print(tokens)

    assert tokens[0].typ=='LINENUMBER'
    assert tokens[1].typ=='LET'
    assert tokens[2].typ=='IDENTIFIER'
    assert tokens[3].typ=='ASSIGN'
    assert tokens[23].typ=='THEN'
    assert tokens[4].typ=='NUMBER'
    assert tokens[-1].typ=='END'

    assert len(tokens)>0

if __name__=='__main__':
    test_lexer()
    print('All tests passed!')

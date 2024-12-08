import re
import sys

spec = [
    ('LET', r'\bLET\b'),
    ('PRINT', r'\bPRINT\b'),
    ('IF', r'\bIF\b'),
    ('THEN', r'\bTHEN\b'),
    ('ELSE', r'\bELSE\b'),
    ('FOR', r'\bFOR\b'),
    ('NEXT', r'\bNEXT\b'),
    ('GOTO', r'\bGOTO\b'),
    ('GOSUB', r'\bGOSUB\b'),
    ('REM', r'\bREM\b'),
    ('END', r'\bEND\b'),
    ('ASSIGN', r'='),
    ('PLUS', r'\+'),
    ('MINUS', r'-'),
    ('TIMES', r'\*'),
    ('DIVIDE', r'/'),
    ('EQ', r'=='),
    ('NEQ', r'<>'),
    ('LT', r'<'),
    ('GT', r'>'),
    ('NUMBER', r'\d+(\.\d+)?'),
    ('IDENTIFIER', r'[A-Za-z][A-Za-z0-9_]*'),
    ('LINENUMBER', r'\d{1,5}'),
    ('SEMI', r';'),
    ('COMMA', r','),
    ('SKIP', r'[ \t]+'),
    ('NEWLINE', r'\n'),
    ('COMMENT', r'REM.*'),
    ('MISMATCH', r'.'),
]

class Token:
    def __init__(self,typ,val,pos):
        self.typ=typ
        self.val=val
        self.pos=pos

    def __repr__(self):
        return f"Token({self.typ},{repr(self.val)},{self.pos})"

class Lexer:
    def __init__(self,w):
        self.w=w
        self.t=self._build_regex()
        self.pos=0

    def _build_regex(self):
        r='|'.join(f'(?P<{t}>{p})' for t,p in spec)
        return re.compile(r)

    def next_token(self):
        if self.pos>=len(self.w):
            return Token('EOF','',self.pos)
        m=self.t.match(self.w,self.pos)
        if not m:
            return Token('MISMATCH',self.w[self.pos],self.pos)
        for k,_ in spec:
            v=m.group(k)
            if v:
                self.pos=m.end()
                if k=='SKIP':
                    return self.next_token()
                elif k!='MISMATCH':
                    return Token(k,v,self.pos)
        return Token('EOF','',self.pos)

def main():
    statements = """
    10 LET X = 10
    20 LET Y = 5
    30 PRINT X + Y
    40 IF X > Y THEN PRINT "X is greater" ELSE PRINT "Y is greater"
    50 REM This is a comment
    60 GOTO 10
    70 END
    """
    lexer=Lexer(statements)
    t=lexer.next_token()
    while t.typ!='EOF':
        print(t)
        t=lexer.next_token()

if __name__=='__main__':
    sys.exit(main())

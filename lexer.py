import re
import sys
from tokens import Token

spec = [
  ('LET', r'\bLET\b'),
  ('PRINT', r'\bPRINT\b'),
  ('IF', r'\bIF\b'),
  ('THEN', r'\bTHEN\b'),
  ('ELSE', r'\bELSE\b'),
  ('FOR', r'\bFOR\b'),
  ('NEXT', r'\bNEXT\b'),
  ('GOTO', r'\bGOTO\b'),
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
  ('LINENUMBER', r'^\d{1,5}\s+'),
  ('NUMBER', r'\d+(\.\d+)?'),
  ('IDENTIFIER', r'[A-Za-z][A-Za-z0-9_]*'),
  ('SEMI', r';'),
  ('COMMA', r','),
  ('STRING_LITERAL', r'"([^"\\]*(\\.[^"\\]*)*)"'),
  ('SKIP', r'[ \t]+'),
  ('NEWLINE', r'\n'),
  ('COMMENT', r'REM.*'),
  ('MISMATCH', r'.'),
]

DEBUG=False

class Lexer:
  def __init__(self,w):
    self.w=w
    self.t=self._build_regex()
    self.pos=0
    self.after_newline=True

  def _build_regex(self):
    r='|'.join(f'(?P<{t}>{p})' for t,p in spec)
    return re.compile(r)

  def next_token(self):
    if self.pos>=len(self.w):
      return Token('EOF','',self.pos)
    m=self.t.match(self.w,self.pos)
    if not m:
      if DEBUG:
        print(f"Lexer error at position {self.pos}: {self.w[self.pos]}")
      return Token('MISMATCH',self.w[self.pos],self.pos)
    for k,_ in spec:
      v=m.group(k)
      if v:
        if DEBUG:
          print(f"Matched {k}: {repr(v)} at position {self.pos}")
        self.pos=m.end()
        if k=='SKIP':
          return self.next_token()
        if k=='NEWLINE':
          self.after_newline=True
          return Token(k,v,self.pos)
        if k=='NUMBER' and self.after_newline:
          self.after_newline=False
          return Token('LINENUMBER',v,self.pos)
        self.after_newline=False
        return Token(k,v,self.pos)
    return Token('EOF','',self.pos)


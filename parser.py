# TODO:
# Take tokens and convert them into an AST (syntax tree)
from tokens import Token

class Parser:
  def __init__(self,tokens):
    self.tokens=tokens
    self.pos=0

  def current_token(self):
    return self.tokens[self.pos] if self.pos < len(self.tokens) else Token('EOF','',self.pos)

  def advance(self): self.pos+=1

  def require(self, typ):
    t=self.current_token()
    if t.typ==typ:
      self.advance()
      return t
    raise SyntaxError(f"Expected {typ}, got {t.typ}")

  def parse(self):
    p=[]
    while self.current_token().typ!='EOF':
      s=self.parse_statement()
      if s:
        p.append(s)
    return p

  def parse_statement(self):
    print("Parse statement!")
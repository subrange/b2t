from tokens import Token

class Parser:
  def __init__(self,tokens):
    self.tokens=tokens
    self.pos=0

  def __repr__(self):
    return f"Parser({repr(self.tokens)})"

  def peek(self):
    return self.tokens[self.pos] if self.pos < len(self.tokens) else Token('EOF','',self.pos)

  def advance(self):
    self.pos+=1

  def skip_newlines(self):
    while self.peek().typ=='NEWLINE':
      self.advance()

  def require(self, typ):
    t=self.peek()
    if t.typ==typ:
      self.advance()
      return t
    raise SyntaxError(f"Expected {typ}, got {t.typ}")

  def parse_program(self):
    p=[]
    while self.peek().typ!='EOF':
      self.skip_newlines()
      s=self.parse_statement()
      if s:
        p.append(s)
    return p

  def parse_statement(self):
    """ single token """
    t=self.peek()
    if t.typ=='LINENUMBER':
      self.advance() # skip labels
      return self.parse_labled_statement()
    else:
      # FIXME: command to the basic interpreter e.g. RUN or LIST
      raise SyntaxError(f"Unexpected token {t.typ} at position {t.pos}")

  def parse_labled_statement(self):
    """ statement prefixed with number """
    t=self.peek()
    if t.typ=='PRINT':
      return self.parse_print_statement()
    if t.typ=='END':
      self.advance()
      return {"type": "End"}
    raise SyntaxError(f"Unsupported statement {t.typ}")

  def parse_print_statement(self):
    """ print statement """
    self.require('PRINT')
    expr=self.parse_expression()
    return {'type': 'Print', 'expression': expr}

  def parse_expression(self):
    t=self.peek()
    if t.typ=='STRING_LITERAL':
      self.advance()
      return {"type": "StringLiteral", "value": t.val}
    else:
      raise SyntaxError(f"Unexpected token {t.typ} at position {t.pos}")


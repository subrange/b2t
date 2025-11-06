class Transpiler:
  def __init__(self,ast):
    self.ast=ast

  def transpile(self):
    ts_code=[]
    for s in self.ast:
      ts_code.append(self.transpile_statement(s))
      return "\n".join(ts_code) # add newline to each statement

  def transpile_statement(self,s):
    if s['type']=='Print':
      return f"console.log({self.transpile_expression(s['expression'])});"
    elif s['type']=='Let':
      # fixme: check type
      return f"let {s['identifier']}: number = {self.transpile_expression(s['expression'])};"
    elif s['type']=='End':
      return "// End of program"
    else:
      raise ValueError(f"Unknown statement type {s['type']}")

  def transpile_expression(self,e):
    if e['type']=='StringLiteral':
      return e['value']
    elif e['type']=='Number':
      return str(e['value'])
    elif e['type']=='Identifier':
      return e['name']
    else:
      return ValueError(f"Unknown expression type {e['type']}")


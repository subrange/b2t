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
    elif s['type']=='End':
      print("End?")
      return "// End of program"

  def transpile_expression(self,e):
    if e['type']=='StringLiteral':
      return e['value']


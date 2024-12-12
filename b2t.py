import sys

from lexer import Lexer
from parser import Parser
from transpiler import Transpiler

def main():
  if len(sys.argv)!=3:
    print("usage: python b2t.py <input.bas> <output.ts>")
    sys.exit(1)

  input_file=sys.argv[1]
  output_file=sys.argv[2]

  if not input_file.endswith('.bas'):
    print("error: input file must end in .bas")

  try:
    with open(input_file,'r') as f:
      statements=f.read().strip()
  except FileNotFoundError:
    printf(f"error: file {input_file} not found!")

  lexer=Lexer(statements)
  tokens=[]
  token = lexer.next_token()
  while token.typ!='EOF':
    tokens.append(token)
    token=lexer.next_token()

  parser=Parser(tokens)
  ast=parser.parse_program()

  transpiler=Transpiler(ast)
  ts_code=transpiler.transpile()

  with open(output_file,'w') as f:
    f.write(ts_code)

if __name__ == '__main__':
  sys.exit(main())


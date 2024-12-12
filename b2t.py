def main():
  import sys
  if (sys.len>1):
    filename=sys.argv[1]
    with open(filename,'r') as f:
      s=f.read()
  else:
    s=input("BASIC commands:")
  # TODO: handle the statements
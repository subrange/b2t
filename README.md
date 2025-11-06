# b2t

https://github.com/microsoft/GW-BASIC

### A BASIC to TypeScript Transpiler

**b2t** is a Python-based transpiler that converts BASIC code to TypeScript.

### Usage

```bash
python b2t.py input.bas output.ts
```

- input.bas: The input file containing BASIC code.
- output.ts: The output file where the transpiled TypeScript code will be written.

### Running Transpiled Code

After generating TypeScript code, you can execute it using `tsx`:

```bash
npm install -D tsx
npx tsx src/index.ts
```

### References

- [32-bit Real Numbers in BASIC](http://ctp.mkprog.com/en/basic/32bit_real_number/)
- [BASIC Operators - Rocket Software](https://www3.rocketsoftware.com/rocketd3/support/documentation/d3nt/91/refman/pickbasic-flashbasic/basic_operators.htm)
- [BASIC Program Flow Control](https://picaxe.com/basic-commands/program-flow-control/)
- [Lexing Basics (Cornell CS)](https://www.cs.cornell.edu/courses/cs4120/2022sp/notes.html?id=lexing#:~:text=This%20approach%20turns%20out%20to,them%20as%20fast%20as%20possible.&text=Do%20you%20see%20the%20problem%20with%20this%20code%3F)
- [Definite Clause Grammars](https://info-ruc.github.io/nlp20/dcg.pdf)
- [BASIC Programming on Wikibooks](https://en.wikibooks.org/wiki/BASIC_Programming)


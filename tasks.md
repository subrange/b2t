# Tasks for Building a Transpiler

https://en.wikipedia.org/wiki/GW-BASIC

## 1. Lexical Analyzer (Tokenizer)
- [ ] Implement a lexical analyzer to split the input code into "tokens" (also known as "lexemes").
  - [ ] Use a while loop with string comparisons or regular expressions for tokenization.
  - [ ] Define the token types (e.g., keywords, operators, identifiers, literals).

## 2. Parser
- [ ] Implement a parser to process the list/stream of tokens.
  - [ ] Create an Abstract Syntax Tree (AST) based on a predefined grammar.
  - [ ] Use a parsing technique, such as **recursive descent**, to build the AST.
  - [ ] Ensure the AST accurately represents the semantics of the program.

## 3. Backend Code Generation
- [ ] Implement the backend to translate the AST into your target language.
  - [ ] Option 1: Translate the AST into an intermediate AST that represents the target language.
  - [ ] Option 2: Directly generate code from the source AST and convert it into the target language.
  - [ ] Ensure the generated code is syntactically correct and can be compiled or interpreted by the target language's tools.

## 4. Testing and Debugging
- [ ] Test the transpiler with simple example programs in the source language.
  - [ ] Verify that the tokenization, parsing, and code generation steps work as expected.
  - [ ] Debug any issues that arise during the translation process.
- [ ] Validate the output code by running it in the target environment.
  - [ ] Ensure the behavior of the generated code matches the intended behavior of the original code.


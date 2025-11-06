# Basic Dialects

https://en.wikipedia.org/wiki/BASIC

There are so many different dialects because there is no standard.

1. What dialect I'm I choosing?
  [Tiny BASIC](https://en.wikipedia.org/wiki/Tiny_BASIC) is a minimalist version of the BASIC programming language.
2. Examples

PRINT -> console.log

LET A = 15
A = 15
-> let A: number = 15;

10 FOR I = 1 TO 10
20 PRINT I
30 NEXT I
40 END
->
for (let i = 1; i <= 10; i++) {
    console.log(i);
}

10 INPUT "WHAT IS YOUR NAME? ", A$
20 PRINT "HELLO "; A$
30 END

let name = prompt("WHAT IS YOUR NAME?");
console.log("HELLO " + name);

10 INPUT "ENTER A NUMBER: ", N
20 IF N > 10 THEN PRINT "LARGE"
30 IF N <= 10 THEN PRINT "SMALL"
40 END

let n = Number(prompt("ENTER A NUMBER:"));
if (n > 10) {
    console.log("LARGE");
} else {
    console.log("SMALL");
}

etc...
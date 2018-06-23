# Unit 0
key topics:
- abstraction
- course roadmap

Abstraction is of course one of the core ideas of progress and computer science overall. Providing a clean interface that allows one to interact with a set of functionality without needing to know HOW it works.

The course is we are going to build the basic components of a computer chipset, then an assembler to run basic code on the machine. Using a hardware descriptive language

# Unit 1
key topics:
- boolean algebra
- boolean functions
- truth tables

## UNIT 1.1
Boolean function: accepts variables and applies boolean algebra (AND, OR, NOT)
Boolean identies:
commutative laws...
- (X OR Y) = (Y OR X)
- (X AND Y) = (Y AND X)
associative laws...
- (X AND ( Z AND Y)) = ((X AND Y) AND Z)
- (X OR (Z OR Y) = ((Z OR Y) OR X))
distrubutive laws...
- (X AND (Y OR Z)) = (X AND Y) OR (X AND Z)
- (X OR (Y AND Z)) = (X OR Y) AND (X OR Z)
De Morgan Laws:
- NOT(X AND Y) = NOT(X) OR NOT(Y)
- NOT(X OR Y) = NOT(X) AND NOT(Y)

## UNIT 1.2
How to go from truth table to boolean expression:
- dijunctive normal form
    - write expression for each row that gives one
    - then or them together
- all boolean functions are represented with OR, AND, and NOT
- but really just AND and NOT, and really you can just use NANDS
- build a whole freaking computer with NANDS!!!!

## UNIT 1.3
- gate logic

Gate logic...
- logic gate is a hardware primitive (OR, NAND, etc.)
- composite logic gate is a ocmbination of primitives/elementary gates
- can describe gates with diagram, functionally, or truth table

Composite gates...
- a three input and gate can be built from two and gates
- this is a basic 'chip'
- gate interface is the gate abstraction == 'what'
- gate implementation is the 'how'
- the interface is _unique_; many implementations
- one abstraction with many implementations
- circuit implementations represent 'chip' as a circuit

## UNIT 1.4
- hdl = hardware description
- start from truth table
- gate == chip
- using a custom HDL similiar to verilog in this course

## UNIT 1.5
simulation modes...
- interactive
- script based

players...
- architect 
- developers

chip design...
- chip API
- test script
- compare file

## UNIT 1.6
- multi-bit buses / bit arrays

## UNIT 1.7
what is a multiplexor? allows you to select and pass certain signals depending on selection input
a demultiplexor distributes an input to a given output

## UNIT 1.8
- you can use Nor instead of Nand to build a computer
- there are other possibilities as well

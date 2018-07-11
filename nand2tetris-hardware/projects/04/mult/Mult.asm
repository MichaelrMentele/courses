// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

	@sum
	M=0

	@R1
	D=M

	@count
	M=D

(LOOP)
	@count
	D=M
	@END
	D;JEQ // count is 0? goto end
	@R0
	D=M
	@sum
	M=M+D // Add RAM[0] to sum
	@count
	M=M-1 // decrement count
	@LOOP
	0;JMP
(END)
	@sum
	D=M
	@R2
	M=D // write sum to RAM[2]
	@end
	0;JMP

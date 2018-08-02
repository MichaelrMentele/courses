// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

        @8192   // Set A register to size of screen memory segment
        D=A
        @scrn_sz
        M=D     // save # bytes to traverse
(REFRESH)
        @scrn_ptr // keeps track of where we are in range of scrn_sz
        M=0
(LOOP)
        @KBD
        D=M     // get value of kbd register

        @WHITE
        D;JEQ   // goto WHITE if KBD value is 0

        @BLACK
        0;JMP   // else go to black

(BLACK)
        @scrn_ptr
        D=M
        @SCREEN
        A=A+D   // scrn_ptr + screen start in memory == current pixel
        M=-1    // Black it out (-1) is all 1's
        @NEXT
        0;JMP   // start next loop
(WHITE)
        @scrn_ptr
        D=M
        @SCREEN
        A=A+D
        M=0     // Fill with white
        @NEXT
        0;JMP
(NEXT)
        @scrn_ptr
        MD=M+1  // Increment the ptr!
        @scrn_sz
        D=M-D   // screen size - ptr
        @REFRESH
        D;JLE   // refresh ptr if ptr is bigger than screen size
        @LOOP
        0;JMP   // else keep going!

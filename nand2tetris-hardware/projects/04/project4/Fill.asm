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

  @8192
  D=A
  
  @SCRN_SIZE
  M=D

(LOOP)
  // Initialize the screen ctr
  @SCRN_SIZE
  D=M
  
  @SCRN_CTR
  M=D

  // current value of kbd word
  @KBD
  D=M

  // if KDB is 0, write white
  @WHITE
  D;JEQ

  // else write black
  @BLACK
  0;JMP

(DRAW)
  // if offset is <= 0, jmp back to the main LOOP
  @SCRN_CTR
  D=M

  @LOOP
  D;JLE

  // else color, decrement ctr, and continue
  @SCREEN
  D=D+A // calculate current pixel addr

  @PIXEL // store ptr to current pixel in screen
  M=D
  
  @COLOR // get the color
  D=M
  
  @PIXEL // assign the current pixel to the color
  A=M
  M=D

  @SCRN_CTR
  M=M-1

  @DRAW
  0; JMP

(WHITE)
  // set color to white
  @COLOR
  M=0

  @DRAW
  0; JMP


(BLACK)
  // Set color to black
  @COLOR
  M=-1 // -1 is all 1's
  
  @DRAW
  0; JMP
  

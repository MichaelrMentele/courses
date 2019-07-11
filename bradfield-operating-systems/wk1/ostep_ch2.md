- we can pretend to have many CPUs -- this is CPU virtualization where many programs can run simultaneously
- OS virtualizes memory, private address space, can look same as other process memory address but is independent 

What is the responsibility of an operating system?

The goal of an operating systems is to provide a safe way to easily utilize system resources like CPU, memory, and I/O.

It does this through 1) virtualizing resources like CPU, memory, disk, I/O etc. to provide sandbox memory environments and the appearance of multiple CPUs thus enabling 2) concurrency, the illusion of multiple programs running at once interleaved with each other (threads) and 3) a robust file system for persisting data. 

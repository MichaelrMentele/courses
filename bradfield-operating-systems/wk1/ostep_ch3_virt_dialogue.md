- virtualizingt he CPU allows us to enable time sharing of the CPU
- heap is for explicitly requested dynamic data i.e. malloc and free
- the stack is static data allocated during compilation
- stack preallocated space for variables
- process states
    - running
    - ready
    - blocked


     ready  <--- deschedule  running
       \     schedule   --->    ^
        \                      / i/o complete
         \ request I/O        /
          >       blocked    /

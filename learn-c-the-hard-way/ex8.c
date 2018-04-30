#include <stdio.h>

int main(int argc, char *argv[])
{

    if ('0' > 10000000) {
        printf("A zero char is sill a char and mapsto a positive int");
    } else if ("\0") {
        printf("A null char also is non zero...");
        int test = (int) "\0";
        printf("a null char evals to %d", test);
    } else {
        printf("they both eval to 0");
    }
    
}

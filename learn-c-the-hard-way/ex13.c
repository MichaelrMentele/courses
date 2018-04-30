#include <stdio.h>

int main(int argc, char*argv[])
{
    int i = 0;

    // iterate argv -- skip 0 because that's the command name
    for (i=1; i<argc; i++) {
        printf("arg %d: %s\n", i, argv[i]);
    }

    char *states[] = {
        "California", "Oregon", "wa", "texas"
    };

    int num_states = 4;

    for (i = 0; i < num_states; i++)
    {
        printf("state %d: %s \n", i, states[i]);
    }
    return 0;
}

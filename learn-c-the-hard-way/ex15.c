#include <stdio.h>

int main(int argc, char *argv[])
{
    printf("blah");
    // create two arrays
    int ages[] = { 12, 3, 4, 23, 2 };
    char *names[] = {
      "blah", "di", "dah", "diiii", "oohhh"
    };

    // safely get size of ages
    int count = sizeof(ages) / sizeof(int);
    int i = 0;

    // using indexing...
    for(i = 0; i < count; i++) {
      printf("%s has %d years to live\n", names[i], ages[i]);
    }

    printf("----\n");

    // setup pointers to the start of arrays
    // there are different kinds of pointers?
    int *cur_age = ages;
    char **cur_name = names;
    // this doesn't work because names is a pointer to an array of strings
    // I can't say a pointer = another pointer because the compiler expects
    // a value in memory
    // char *cur_name2 = names;
    //printf("The address to the current name is: %s\n", cur_name);
    //printf("%s if I didn't use double **\n", cur_name2);

    // second way using pointers
    // this is using dereferencing to retrieve the value at the
    // pointer address + i

    // char ** is a pointer to a pointer of char types
    for (i = 0; i < count; i++) {
      printf("%s is %d years old\n", *(cur_name + i), *(cur_age + i));
    }

    printf("---\n");

    // third way, pointers are just arrays
    // basically equivalent to cur_name + i with a dereference as above
    for (i = 0; i < count; i++) {
      printf("%s is %d years old again \n", cur_name[i], cur_age[i]);
    }

    printf("---\n");

    // fourth
    // zero out the memory address with cur_age - ages, pointer subtraction
    // this doesn't make sense... this is some arbitrary difference
    // I incremeent both of them... will they ever... ugh
    for (cur_name = names, cur_age = ages; (cur_age - ages) < count; cur_name++, cur_age++) {
      printf("%p\n", ages + 1);
      printf("%s lived %d years so far.\n", *cur_name, *cur_age);
    }

    // a pointer cointains an address in memory in the computer

    return 0;
}

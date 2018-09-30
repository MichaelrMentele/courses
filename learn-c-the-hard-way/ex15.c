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

// A pointer references the value stored at a memory address it contains.
// C thinks your whole computer is one massive array of bytes. C puts types and sizes of those types on TOP of your RAM (giant array of memory).
// When you define an array in c the following happens:
// 1. define a block of memory for that array
// 2. point the name to the beggining of that block
// 3. indexes adds (type size * index) to the base address (the name)
// A pointer is simply an address pointing into the computers memory with a type so you get the right size of data with it. A pointer gives you raw access to a block of memory.
// Useful things you can do with pointers:
// 1. ask OS for a chunk of memory and use pointer to work with it
// 2. pass big mem blocks to functions with a pointer 
// 3. take address of a function to use as a dynamic callback
// 4. scan chunks of memory, converting bytes off of a network socket into data structures or parsing files
//
// Lexicon:
// type *ptr: a pointer of type named ptr
// *ptr the value of whatever ptr is pointed at
// *(ptr + i) the value at ptr + i
// &thing the address of thing
// type *ptr = &thing: a pointer of type named ptr set to the address of thing
// ptr++ increment where ptr points

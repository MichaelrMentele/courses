#include <stdio.h> // gives me the NULL constant but I think that is all
#include <assert.h> // gives me the assert function
#include <stdlib.h> // also gives NULL, malloc, and free I think
#include <string.h> // 

// define a struct with a char array and three named int attributes
// a struct is a data structure composed of other data structures
// can be used for user defined data structures--kind of a primitive object
struct Person {
    char *name;
    int age;
    int height;
    int weight;
};

// define a function that returns a struct of type person??
struct Person *Person_create(char *name, int age, int height, int weight)
{
    // create a struct Person pointer called who
    // allocate it memory of the size of a Person struct
    struct Person *who = malloc(sizeof(struct Person));
    assert(who != NULL); // assert it isn't NULL (otherwise will raise an exception)

    who->name = strdup(name); // access the name attribute space and assign a copy of name
    who->age = age; // access age attr and assign age
    who->height = height;
    who->weight = weight;

    return who; // return the Person pointer 
}


void Person_destroy(struct Person *who)
{
    assert(who != NULL);

    free(who->name);
    //free(who);
}

void Person_print(struct Person *who)
{
    printf("Name: %s\n", who->name);
    printf("\tAge: %d\n", who->age);
    printf("\tHeight: %d\n", who->height);
    printf("\tWeight: %d\n", who->weight);
}

int main(int argc, char *argv[])
{
    // make two people structures
    struct Person *joe = Person_create("Joe Alex", 32, 64, 140);

    struct Person *frank = Person_create("Frank Blank", 20, 72, 180);

    // print them out and where they are in memory
    printf("Joe is at memory location %p:\n", joe);
    Person_print(joe);

    printf("Frank is at mem location %p:\n", frank);
    Person_print(frank);

    // make everyone age 20 years and print them again
    joe->age += 20;
    joe->height -= 2;
    joe->weight += 40;
    Person_print(joe);

    frank->age += 20;
    frank->weight += 20;
    Person_print(NULL); //frank);

    // destroy them both so we clean up
    // Person_destroy(NULL); //joe);
    Person_destroy(frank);

    return 0;
}

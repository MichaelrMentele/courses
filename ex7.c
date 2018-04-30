#include <stdio.h>

int main(int argc, char *argv[])
{
    int distance = 100;
    float power = 2.345f;
    double super_power = 56789.3234;
    char initial = 'A';
    char first_name[] = "michael";
    char last_name[] = "mentele";

    printf("you are %d miles away\n", distance);
    printf("you have %f levels of power \n", power);
    printf("you have %f awsome super powers \n", super_power);
    printf("I have the initial %c\n", initial);
    printf("My first name is %s\n", first_name);
    printf("my last name is %s\n", last_name);
    printf("my whole name is %s %c %s \n", first_name, initial, last_name);

    int bugs = 100;
    double bug_rate = 1.2;

    printf("You have %d bugs at the rate of %f\n", bugs, bug_rate);

    unsigned long universe_of_defects = 1L * 1024L * 1024L * 1024L * 100000000L;
    printf("The entire universe has %ld bugs.\n", universe_of_defects);
    
    double expected_bugs = bugs * bug_rate;
    printf("you are expected to have %f bus \n", expected_bugs);

    double part_of_universe = expected_bugs / universe_of_defects;
    printf("this is only a %e portion of the universe \n",
            part_of_universe);

    //this makes no sense just demo of weirdness
    char nul_byte = '\0';
    int care_percentage = bugs * nul_byte;
    printf("which means you should care %d%%\n", care_percentage);
    // printf("nullbyte with c %c and s %s", nul_byte, nul_byte);
    printf("nullbyte %s" , "blah");

    return 0;
}

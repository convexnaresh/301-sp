#include <stdio.h>
#include <string.h>
#include <stdlib.h>

//$gcc hof.c -o hof -Wall -Werror -g #to run w/o warning and runs.
//this program has a heap buffer overflow error, and AddressSantiz
//$gcc hof.c -o hof -Wall -Werror -g =fsanitize=address
//$./hof #the memory access problem will be identified and a repor

int main(int argc, const char *argv[])
{
    char *msg = "Hello world!";
    char *ptr = NULL;

    ptr = malloc(strlen(msg));

    strcpy(ptr, msg);

    printf("%s\n", ptr);

    return 0;


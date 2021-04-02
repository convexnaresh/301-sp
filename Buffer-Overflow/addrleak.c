#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
int main(int argc, const char *argv[]) {
	    char *s = malloc(100);
	    strcpy(s, "Hello world!");
	    printf("string is: %s\n", s);

	    free(s);//free up the memory allocated
	    //use after free

	    strcpy(s, "Hello, return");

    return 0;
}

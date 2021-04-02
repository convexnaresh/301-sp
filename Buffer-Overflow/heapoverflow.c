#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int main(int argc, const char *argv[]) {
    // whoops, forgot c strings are null-terminated
    // and not enough memory was allocated for the copy
    char *s = malloc(12);
    strcpy(s, "Hello world!");
    printf("string is: %s\n", s);
    free(s);
    return 0;
}

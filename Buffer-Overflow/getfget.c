#include <stdio.h>
#define SIZE_OF_BUFF 5

int main()
{
    char buffer_input[SIZE_OF_BUFF];
    
    //gets(buffer_input);

    
    //safe way
    fgets (buffer_input, SIZE_OF_BUFF, stdin);

    printf("\nYou entered: %s", buffer_input);
    
    return 0;
}

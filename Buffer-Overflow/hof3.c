#include<stdio.h>


#http://etutorials.org/Networking/network+security+assessment/Chapter+13.+Application-Level+Risks/13.5+Heap+Overflows/
int main(void)
{

    char *buff1, *buff2;



    buff1 = malloc(40);

    buff2 = malloc(40);

    gets(buff1);

    free(buff1);

    exit(0);

}

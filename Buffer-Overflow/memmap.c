#include <stdio.h>

char c[]="instructor/faculty";//global variable stored (-->)  Initialized Data Segment in read-write area

const char s[]="hacker/earth";    //global variable stored in Initialized Data Segment in read-only area

char d; //uninitialized var -> bss

int main()
{
    static int i=11; //static variable stored in Initialized Data Segment


    static int j; // uninitialized static variable -> bss

    char *p= (char*) malloc(sizeof(char)); // malloc/calloc -> heap segment

    int x = myfunc(i);
    return 0;
}

//stored, and executed using 'stack'
int myfunc(int k){

	int z=100; //stack
	
	return z;
}

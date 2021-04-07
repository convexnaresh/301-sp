// fortify_test.c
#include<stdio.h>
#include<string.h>

int main(int argc, char **argv) {
	char buffer[5];
	printf ("Buffer Contains: %s , Size Of Buffer is %d\n",
                               buffer,sizeof(buffer));
	// Here the compiler the length of string to be copied
	strcpy(buffer,"de");
	//strcpy(buffer, argv[1]); //runtime length
	printf ("Buffer Contains: %s , Size Of Buffer is %d\n",
                               buffer,sizeof(buffer));
}

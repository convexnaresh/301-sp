//filename: sof.c
#include<stdio.h>

void f(int a, int b, int c){
	char buffer1[10];
	char buffer2[5];
	

	strcpy(buffer1, "AAAAAAAAAAAAAAAAAAAAAAAAAAAAaa");
	
	printf("%s\n",buffer1);
	strcpy(buffer2, "BBBB");
	printf("%s\n",buffer1);
	printf("%s\n", buffer2);
	
}

void main() {
      f(1,2,3);
}


#include <stdio.h>

/*
compile:
	$gcc -o eg1 eg1.c

	//disable compile time overflow detection
	
	$gcc -fno-stack-protector -z execstack -o eg1 eg1.c
view memory:
	$size eg1

execute:
	$./eg1
	Your command? ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZz

view assembly:
	$gdb eg1
	(gdb)disas main
*/

int main(int argc, char* argv[]) {

      	char command[20];  // Only 10 bytes for command (including termination char)
      	printf("Your command?\n");


      	gets(command);  // gets provides no protection against buffer overflow

       	printf("Your command was: %s\n", command);
}


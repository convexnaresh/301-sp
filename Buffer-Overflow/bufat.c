#include <string.h>
#include <stdio.h>

main(){
       	char name[40];
        printf("What is your name?\n");
       	gets(name);//scanf("%s", name);
	
	
        bo(name, "uname -a");
}

int bo(char *name, char *cmd){
        char c[40];
        char buffer[40];
        
	printf("Name buffer address:    %x\n", buffer);
        printf("Command buffer address: %x\n", c);
        
	strcpy(c, cmd);
        strcpy(buffer, name);
        
	printf("Goodbye, %s,%d\n", buffer,sizeof(buffer));

        printf("Executing command:%s\n", c);
        fflush(stdout);
        system(c);
}

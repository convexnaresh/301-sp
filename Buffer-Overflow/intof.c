int main(){
	int x=1073741824;
	printf("%d",8*x);
	printf("%d",4294967295+1);
	char *ptr;

	ptr = malloc(x*sizeof(char));

	//memset(ptr,0,x*sizeof(char*));
	strcpy(ptr, "hello, I am big string");

	printf("%s",ptr);
}

#include <stdio.h>

//trying to pass a size of 64 bytes to a smaller heap buffer of 32 byptes

int main(int args, char** argv) {
  void* heap = (void*) malloc(32);
  memset(heap, 'A', 64);
  printf("%s\n", heap);
  free(heap);
  heap = NULL;
  return 0;
}

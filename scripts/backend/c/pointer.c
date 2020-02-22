#include <stdio.h>


int main(void) {
  printf("count of memory space int type occupying: %d\n", sizeof(int));

  int a;
  a = 10;

  int *pa;
  pa = &a;

  printf("%d\n", *pa);

  return 0;
}

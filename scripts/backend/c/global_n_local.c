#include <stdio.h>


int a = 10; // global

void f(void) {
  // local
  int a = 1;
  a++;
  printf("[local]a: %d\n", a);
}

int main(void) {
  f();

  printf("[global]a: %d\n", a);

  return 0;
}

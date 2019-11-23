#include <stdio.h>

void f(void) {
  static int a = 0; // 静的変数
  a++;
  printf("a:%d\n", a);
}

void g(void) {
  int b= 0; // 自動変数
  b++;
  printf("b:%d\n", b);
}

int main(void) {
  f();
  f();
  f();

  g();
  g();
  g();
  return 0;
}

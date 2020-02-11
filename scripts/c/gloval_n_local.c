#include <stdio.h>

// 変数の有効範囲

int a = 10; // グローバル変数

void f(void) {
  // ローカル変数
  int a = 1;
  a++;
  printf("[local]a: %d\n", a);
}

int main(void) {
  f();

  printf("[global]a: %d\n", a);

  return 0;
}

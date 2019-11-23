#include <stdio.h>

// 配列

int main(void) {
  int sales[3];

  sales[0] = 200;
  sales[1] = 400;
  sales[2] = 300;

  int sales2[] = {300, 414, 345};

  printf("%d\n", sales[1]);
  printf("%d\n", sales2[1]);
  return 0;
}

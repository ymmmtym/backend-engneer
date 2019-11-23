#include <stdio.h>

// switch文

int main(void) {
  static int rank = 7;
  // 静的変数：宣言は最初の１回のみ適用される

  switch(rank){
    case 1:
      printf("gold\n");
      break;
    default:
      printf("bad\n");
  }
  return 0;
}

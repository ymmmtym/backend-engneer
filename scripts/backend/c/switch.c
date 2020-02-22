#include <stdio.h>

// switch

int main(void) {
  static int rank = 7;

  switch(rank){
    case 1:
      printf("gold\n");
      break;
    default:
      printf("bad\n");
  }
  return 0;
}

#include <stdio.h>

//while

int main (void){
  int m = 0;
  while(m < 10){
    printf("m: %d\n", m);
    m++;
  }

// do...while処理はあと判定なので、条件に合致しなくても最低１回は実行される
  int n = 0;
  do{
    printf("n: %d\n", n);
    n++;
  } while(n < 15);

  int x = 0;
  for (x = 0; x < 10; x++) {
    if (x == 3) {
      continue;
    }
    if (x == 8) {
      break;
    }
    printf("x: %d\n", x);
  }

  return 0;


}

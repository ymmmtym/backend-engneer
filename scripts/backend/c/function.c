#include <stdio.h>

// 関数
// 返り値の型 関数名(引数,...){
// 処理;
// return 返り値;
// }

// 関数を追加する場合は、１番上にプロトタイプ宣言を書く
float getMax(float a, float b);
void sayHi(void);


// 返り値がある関数
float getMax(float a, float b){
  if(a >= b){
    return a;
  } else{
    return b;
  }
/* 三項演算子を用いて下記のように代用可能
  return (a >= b) ? a: b;
*/
}


// 返り値がない関数
void sayHi(void){
  printf("hi!\n");
}

// main関数
int main(void) {
  float result;
  result = getMax(2.3, 5.2);
  printf("%f\n", result);

  sayHi();

  return 0;
}

#include <stdio.h>

float getMax(float a, float b);
void sayHi(void);


float getMax(float a, float b){
  if(a >= b){
    return a;
  } else{
    return b;
  }
}


// no return value
void sayHi(void){
  printf("hi!\n");
}

// main function
int main(void) {
  float result;
  result = getMax(2.3, 5.2);
  printf("%f\n", result);

  sayHi();

  return 0;
}

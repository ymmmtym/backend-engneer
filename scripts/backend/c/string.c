#include <stdio.h>

// 文字列:charの配列、終端は\0

// 以下は全て同様の文字列となる
char s1[] = {'a', 'b', 'c', '\0'};
char s2[] = "abc";
char s3[] = "abc";


int main(void) {
  char s[] = "abc";
  printf("%c\n", s[1]);
  return 0;
}

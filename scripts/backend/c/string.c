#include <stdio.h>

char s1[] = {'a', 'b', 'c', '\0'};
char s2[] = "abc";
char s3[] = "abc";


int main(void) {
  char s[] = "abc";
  printf("%c\n", s[1]);
  return 0;
}

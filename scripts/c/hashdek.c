#include <stdio.h>
#include <string.h>

unsigned long hashdek (unsigned char *str, int len);

int main (void) {
  char s[20];
  scanf("%s", s);
  printf("%ld\n", hashdek(s, strlen(s)));
  return 0;
}

unsigned long hashdek (unsigned char *str, int len) {
  unsigned long hash;
  printf("   len: %d\n", len);
  for (hash=len; len--; ) {
    printf("  %d: %c: %o", len, *str, *str);
    printf("  <<5: %d, >>27: %d ^:%d , str:%d ", hash<<5, hash>>27, (hash<<5)^(hash>>27), *str);
    hash = ((hash<<5)^(hash>>27))^*str++;
    printf("   %d:%lo\n", len, hash);
  }
  return hash;
}

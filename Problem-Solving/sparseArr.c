#include <stdio.h>
#include <string.h>
int main() {

  int strings_count, queries_count, count = 0, i, j, s;
  char strings[10000][20], queries[10000][20];
  scanf("%d", &strings_count);
  for (j = 0; j < strings_count; j++) {
    scanf("%s", strings[j]);
  }
  scanf("%d", &queries_count);
  for (i = 0; i < queries_count; i++) {
    scanf("%s", queries[i]);
  }
  for (i = 0; i < queries_count; i++) {
    count = 0;
    for (j = 0; j < strings_count; j++) {
      s = strcmp(queries[i], strings[j]);
      if (s == 0) {
        count = count + 1;
      }
    }
    printf("%d\n",count);
  }
return 0;
}

#include <stdio.h>

int a[] = {43, 96, 69, 13, 21, 7, 66, 69, 99, 1};
int n = sizeof a / sizeof a[0];

void swap(int *a, int *b) {
  int t;
  t = *a;
  *a = *b;
  *b = t;
}

int main () {
  /* sort */
  int i, j = n, k;
  while (j > 1) {
    k = 1;
    for (i = 0; i < j - 1; i++) {
      if (a[i] > a[i + 1]) {
        swap(&a[i], &a[i+1]);
        k = i+1;
      }
    }
    j = k;
  }
  /* print result */
  for (i = 0; i < n; i++)
    printf("%d%s", a[i], i == n - 1 ? "\n" : " ");
}

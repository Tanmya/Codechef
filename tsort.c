
#include <stdio.h>
 
void bubble_sort(int [], int);
 
int main()
{
  int array[100001], n, c, d, swap;
  scanf("%d", &n);
 
  for (c = 0; c < n; c++)
    scanf("%ld", &array[c]);
 
  bubble_sort(array, n);
 
  for (c = 0; c < n; c++)
     printf("%ld\n", array[c]);
 
  return 0;
}
 
void bubble_sort(int list[], int n)
{
  int c, d, t;
 
  for (c = 0 ; c < n - 1; c++)
  {
    for (d = 0 ; d < n - c - 1; d++)
    {
      if (list[d] > list[d+1])
      {
        t         = list[d];
        list[d]   = list[d+1];
        list[d+1] = t;
      }
    }
  }
}

#include <stdio.h>

int main()
{
  int t1 = 0;
  int t2 = 1;
  int a;
  printf("Enter your limit:\n");
  scanf("%d", &a);
  printf("\n%d %d ",t1,t2);
  for (int i = 2; i < a; i++)
  {
    int nextT = t1 + t2;
    printf(" %d",nextT);
    t1 = t2;
    t2 = nextT;
  }
}
#include<stdio.h>
int main()
{ char Original[20], Reversed[20];
int start, end , count=0;
printf("Enter Your String:\n");
gets(Original);
while (Original[count]!='\0')
  count++;
end = count -1;
    for(start=0;start<count;start++){
        Reversed[start]= Original[end];
        end--;
    }
    Reversed[start]='\0';

   printf("Reversed string: %s\n",Reversed);

    
    return 0;
}
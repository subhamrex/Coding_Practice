#include<stdio.h>
#include<string.h>
int main()
{
    char Original[] ="Anjan";
    char Rev[20];
    
    int i =0,len=strlen(Original)-1;
    int l =len;
     while(i<len){
         if(Original[i++]!= Original[len--]){
             printf("not palindrome\n");
             for(int j =l,k=0;j>=0;j--){
                 Rev[j]=Original[k++];
                
             }
             Rev[l+1]='\0';
             printf("%s",Rev);
             return 0;
         }
        
         
     }
             printf("palindrome");
}
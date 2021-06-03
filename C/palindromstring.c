#include<stdio.h>
#include<string.h>
int main()
{ 
    char name[10];
    printf("Enter your string:\n");
    gets(name);
    char original[10];
    strcpy(original,name);
    strrev(name);
    printf("%s\n",name);

    if(strcmp(original,name)==0){
        printf("%s is palindrome of %s",original,name);
    }
    else
    {
        printf("%s is not palindrome of %s",original,name);
    }
    
    
    return 0;
}
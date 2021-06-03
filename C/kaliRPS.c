#include <time.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char ch_arr[3][11] = {"Paper","Scissors","Rock"};

void decision(int nMax,int nMin,int userI)
{
int compI;
srand(time(NULL));
int num = rand()%((nMax+1)-nMin) + nMin;
puts(ch_arr[num]);
compI=num;
printf("%d",userI);
printf("%d",num);

switch(compI)
{

case 0:
if(userI==0)
{
printf("TIE");
}
else if(userI==2)
{
printf("USER WINS");
}
else
{
printf("COMPUTER WINS");
}
break;
case 1:
if(userI==0)
{
printf("COMPUTER WINS");
}
else if(userI==1)
{
printf("TIE");
}
else
{
printf("USER WINS");
}
break;
case 2:
if(userI==0)
{
printf("USER WINS");
}
else if(userI==1)
{
printf("COMPUTER WINS");
}
else
{
printf("TIE");
}
break;
}
}


void main()
{
int index=0;
char* user;
while(1)
{
printf("Enter Your Choice Player 1 : ");
gets(user);
for(int i=0;i<3;i++)
{
 if(strcmp(user,ch_arr[i])==0)
 {
 index=i;
 }
}
decision(2,0,index);

}
}

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int userchoice(int U){
    if (U == 0)
    {
        printf("Rock\n");
    }
    else if (U == 1)
    {
        printf("Paper\n");
    }
    else if (U== 2)
    {
        printf("Scissors\n");
    }
    return U;
}

int generateRandomNumber()
{
    srand(time(NULL)); //srand takes seed as an input and is defined inside stdlib.h
    int ResultC = rand() % 2;
    if (ResultC == 0)
    {
        printf("Rock\n");
    }
    else if (ResultC == 1)
    {
        printf("Paper\n");
    }
    else if (ResultC == 2)
    {
        printf("Scissors\n");
    }

    return ResultC;
}
int battle(int user,int comp,char name[]){
    if(user==0 && comp==0 ||user==1 && comp==1 || user==2 && comp==2){
        printf("Match draw\n");
    }
    else if(user==1 && comp==0){
        printf("%s wins",name);
    }
    else if(user==0 && comp==1){
        printf("Opponent wins");
    }
     else if(user==2 && comp==0){
        printf("%s wins",name);
    }
     else if(user==0 && comp==2){
        printf("Opponent wins");
    }
     else if(user==1 && comp==2){
        printf("Oppnents wins");
    }
     else if(user==2 && comp==1){
        printf("%s wins",name);
    }

}
//Create Rock, Paper & Scissors Game
// Player 1: rock
// Player 2 (computer): scissors 

// rock vs scissors - rock wins
// paper vs scissors - scissors wins
// paper vs rock - paper wins
// Notes: You have to display name of the player during the game. Take users name as an input from the user.

int main()

{
    char name[10];
    int U;
    printf("Enter User Name: ");
    gets(name);
    printf("0 for Rock\n1 for Paper\n2 for scissors\n");
    printf("%s's choice\n ", name);
    scanf("%d",&U);
    int user = userchoice(U);
    printf("%d\n",user);
    printf("Opponent's Choice is ");
    int comp = generateRandomNumber();
    printf("%d\n",comp);
    battle(user,comp,name);
    return 0;
}

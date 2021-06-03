from random import *
name =input("What is your name\
?\n") #\ for line continution
print(f"Hello {name}, choose a no between 0 to 20")
myGresult=0
secretNo=randint(0,20)
for i in range(0,6):
    print("Take a guess:")
    guessNo = int(input())
    if(guessNo>secretNo):
        print("Your choosen no is high")
    elif(guessNo<secretNo):
        print(("Your choosen no is low"))    
    else:
        myGresult = guessNo
        break
if(myGresult==secretNo):
    print("You choosed corretly")
else:
    print(f"You are wrong, correct no is {secretNo}")    

                

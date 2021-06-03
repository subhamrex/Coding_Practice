A="aaBabcDaAXXXxYyyZZzzzzz"
SA={}
CA={}
Result=[]   
counterA = 0   
counterB = 0
for i in A:
    if i.islower():
        counterA +=1
        SA[i]=counterA
    if i.isupper():
        counterB +=1
        CA[i]= counterB  
print(SA)      
print(CA)  
for i in CA:
    for j in SA:
        if j.upper() == i:
            Result.append(i)
if Result==[]:
    print("No")
else:                
    print(Result)   
    print(max(Result))
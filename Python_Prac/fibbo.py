n = int(input("How many times?" ))
n1 ,n2 = 0,1
count = 0
if n <=0:
    print("Plz Enter postive no")
elif n ==1:
    print(n1)
else:
    while( count < n):
        print(n1)  
        n_th = n1 + n2
        n1 = n2
        n2 = n_th
        count +=1


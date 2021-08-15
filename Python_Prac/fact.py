n = int(input("Enter your no: "))

fact = 1

if n < 0:
    print("Factorial doesn't exist for negative no")
elif n == 0:
    print(fact)    
else:
    for i in range(1,n+1):
        fact = fact * i    
    print(fact)    

'''
def rec_fact(n):
    if n == 1:
        return n
    else:
        return n* rec_fact(n-1)    
'''    
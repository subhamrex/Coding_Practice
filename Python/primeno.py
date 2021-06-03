X = int(input(" Enter Lower Limit: "))
Y = int(input(" Enter Higher Limit: "))
print("Prime numbers between", X, "and", Y, "are:")
for i in range(X,Y+1):
    if (i > 1):
        for j in range(2,i):
            if (i % j==0):
                break
        else:
            print(i)  
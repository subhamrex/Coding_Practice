A = [1,5,6,8,0]
sm = A[0]
pos = 0
for i in range(len(A)):
    if(sm>A[i]):
        sm = A[i]
        pos = i
print(sm)        
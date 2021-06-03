def sol(A):
    N = len(A)
    res = [0]*N
    start=0
    end = N-1
    for i in range(N):
        if A[i] %2 ==0:
            res[start] = A[i]
            start +=1
        else:
            res[end] = A[i]
            end -=1
    return res

A = [3,1,2,4]
print(sol(A))        
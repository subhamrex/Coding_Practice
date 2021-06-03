#Find an index in an array such that its prefix sum equals its suffix sum.
A = [-1, 3,-4,5,1,-6,2,1]

def find_index(A):
    n = len(A)
    if n == 0:
        return -1
    
    for i in range(n):
        sum_left = 0
        sum_right = 0
        mm = 0
        for j in range(n):
            if(mm<A[j]):
                mm = A[j]
        for j in range(i):
            sum_left +=A[j]     
        for j in range(i+1,n): 
            sum_right +=A[j]
            
        if (sum_left == sum_right):
            return i
    return -1        
  
print(find_index(A))                  

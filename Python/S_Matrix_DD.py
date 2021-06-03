
# Find the abs value of subs of left_right diagonal sum and right_left diagonal sum
def diagonalDifference(arr,n):
    DL_sum = 0
    DR_sum = 0
    for i in range(n):
        for j in range(n):
            if (i == j):
                DL_sum = DL_sum + arr[i][j] #Left to right
            if((i+j) == (n-1)):
                DR_sum = DR_sum + arr[i][j] #right to left
                
                

    return abs(DL_sum - DR_sum)

arr=[[11,2,4],
    [4,5,6],
    [10,8,-12]]    
n = 3 # no of row and col
print(diagonalDifference(arr,n))
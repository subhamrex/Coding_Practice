def diagonal(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            if (i+j) == (n-1):
                print(arr[i][j],end=", ")
    print()
                

arr = [[4,6,7,9],[5,0,1,3],[6,3,9,8],[1,5,3,8]]
diagonal(arr)
def miniMaxSum(arr):       
    sumNo=[0]*(len(arr))
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i!=j:
                sumNo[i]=sumNo[i]+arr[j]
    print(f"{min(sumNo)} {max(sumNo)}")        
        
        

#arr = list(map(int, input().strip().split()))
arr =[0,5,1,5,5]
miniMaxSum(arr)
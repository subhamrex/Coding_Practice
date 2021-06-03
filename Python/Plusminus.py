def plusminus(arr):
    m =len(arr)
    CountP=0
    CountN =0
    Count0=0
    for i in arr:
        if i <0:
            CountN +=1
        if i>0:
            CountP +=1
        if i==0:
            Count0 +=1
    print(CountP/m)
    print(CountN/m)  
    print(Count0/m)              
            
n = int(input())
arr = list(map(int, input().strip().split()))[:n]
plusminus(arr)
   
    
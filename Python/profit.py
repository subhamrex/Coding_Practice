rows,cols = input().split()
rows = int(rows)
cols = int(cols)
Arr=[]
for i in range(rows):
    ar = list(map(int, input().strip().split(' ')))
    Arr.append(ar)
#print(Arr)
minProfit=[]
for col in range(cols):
    temp=[]
    for row in range(rows):
        a = Arr[row][col]
        temp.append(a)
    minProfit.append(min(temp))    
#print(minProfit)    
for i in range(len(minProfit)):
    print(minProfit[i],end=" ")   
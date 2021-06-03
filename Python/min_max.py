a1= int(input())
a2= int(input())
a3= int(input())

Arr=[]
def digitMinMax(a1, a2, a3):
    for i in range(len(a1)):
        temp=[]
        temp.append(int(a1[i]))
        temp.append(int(a2[i]))
        temp.append(int(a3[i]))
        Arr.append(temp) 
    for i in range(len(Arr)):  
        result = min(Arr[i])  if i%2==0 else max(Arr[i])
        print(result,end=" ")   
    
if(a1>=1000) and (a1<9999) and (a2>=1000) and (a2<9999) and (a3>=1000) and (a3<9999):
    digitMinMax(str(a1),str(a2),str(a3))
    
else:
    print("Not found")    

    
    
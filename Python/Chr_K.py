def K_Chr(N,Str,Q,query):
    conStrPos=[]
    for i in range(Q):
        L = query[i][0]
        R = query[i][1]
        K = query[i][2]
        
        if L!=R:
            conStr= Str[L-1] + Str[R-1]
            conStrPos.append(conStr[K-1])
        if L==R:
            conStr = Str[L-1]   
            conStrPos.append(conStr[K-1]) 
        if L ==0 or R==0 or K==0:
            return 'Wrong Position'   
    return conStrPos   
            

N = int(input())
Str=[]
for i in range(N):
    arr = input()
    Str.append(arr)
    
print(Str)  
Q = int(input())
query = []
for i in range(Q):
    arr = list(map(int, input().strip().split(' ')))
    query.append(arr) 
    
#print(query) 

out = K_Chr(N,Str,Q,query)
if out != 'Wrong Position':
    for i in range(len(out)):
        print(out[i])
else:
    print(out)        
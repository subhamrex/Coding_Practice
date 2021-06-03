def rev_Arr(a):
    temp=[]
    for i in range((len(a)-1),-1,-1):
        temp.append(a[i])  
    return temp
         

if __name__ == '__main__':
    Arr = list(map(int, input().strip().split(' ')))
    res=rev_Arr(Arr)
    print(res)
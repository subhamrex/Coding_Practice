def selectionsort(list):
    for i in range(len(list)-1):
        minpos=i
        for j in range(i,len(list)):
            if list[j] < list[minpos]:
                minpos=j
                
        list[i],list[minpos]=list[minpos],list[i]        
                
if __name__=='__main__':
    list = [100,45,23,999,1]    
    selectionsort(list)   
    print(list)
def heapsort(list):
    length = len(list)
    for i in range(((length//2)-1),-1,-1):
        heapify(list,length,i)
        
    #swap the element heapify again
    for i in range((length -1),-1,-1):
        list[0],list[i] = list[i],list[0]
        heapify(list,i,0)
        

def heapify(list,n,i):
    largest = i #parent node index pos
    li=2*i+1 #Left child node index pos
    ri = 2*i+2    #Right child node index pos   
    
    if(li<n and list[li] >list[largest]):
        largest = li
        
    if(ri<n and list[ri] >list[largest]):
        largest = ri    
    if (largest!=i):
        list[i],list[largest]=list[largest],list[i]    
        heapify(list,n,largest)
        
def printlist(list):
    for i in range(0,len(list)):
        print(list[i],end=" ")
      

if __name__ =='__main__':
    list = [22,13,71,40,12,14,100,20]
    heapsort(list)
    printlist(list)
def bubble_sort(list):
    size = len(list)
    for i in range(size -1):
        swap= False
        for j in range(size-1-i):
            if list [j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
                swap = True
        if not swap:
            break            
            
        
    

if __name__ == '__main__':
      
    list = [99,10,55,100,14,30,145,9]
    bubble_sort(list)
    print(list)

from util import time_it

@time_it
def linear_search(list, search):
    for index, element in enumerate(list):
        if element is search:
            print(f"found {search} at index {index} using Linear search")
            break
    else:
        print("Not found using Linear search")

@time_it
def binary_search(list, search):
    left_index = 0
    right_index = len(list)-1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (right_index + left_index)//2
        mid_no = list[mid_index]

        if mid_no == search:
            print(f"found {search} at index {mid_index}")
            break

        if mid_no < search:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    else:
        print("Not found using Binary search")
                
def recur_binary_search(list, search,left_index,right_index):
    if right_index < left_index:
        return -1
    mid_index = (right_index + left_index)//2
    if mid_index >=len(list) or mid_index <0:
        return -1
    mid_no = list[mid_index]
    
    if mid_no == search:
        return mid_index
    
    if mid_no < search:
            left_index = mid_index + 1
    else:
        right_index = mid_index - 1
    return recur_binary_search(list,search, left_index,right_index)    
        
        
    


if __name__ == '__main__':
    list = [10, 15, 50, 55, 96, 100]
    search = 100
    index = recur_binary_search(list,search,0,(len(list)-1))
    if index == -1:
        print("not found")
    else:
        print(f"{search} found at index {index} using recur_binary_search")    

    linear_search(list, search)
    binary_search(list, search)

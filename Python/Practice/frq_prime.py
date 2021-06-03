def frq_prime(input_list):
    print(input_list)

if __name__ == '__main__':
    n = int(input("Enter no of cases: "))
    input_list=[]
    for i in range(n):
        a = list(map(int,input().strip().split(' ')))
        input_list.append(a)
             
    
    frq_prime(input_list)           
            
    
    
    
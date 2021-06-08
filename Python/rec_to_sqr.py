# Convert Rectangle to Squares. Find the total no of squares to be formed.

def rec_to_sqr(M,N):
    if M == N: 
        return M // N
    else:
        i = N
        store = 0
        counter = 0
        while(i < M):
            if M > store:
                store = store + N
                counter = counter + 1
                i =  i + store   
                #print(store)
                
            else:
                break    
              
        #print(counter) 
        #print(store)  
        left = M - store

        if N % 2 == 0 and (left == 3):
            counter = counter + (N//2) + N    
            return counter  

        else:
            counter = counter + N
            return counter       
        
if __name__ == '__main__':
    M = int(input())
    N = int(input())
    print(rec_to_sqr(M,N))
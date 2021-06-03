#Breaking the Records

def breakingRecords(scores):
    Hi=scores[0]
    Low=scores[0]
    count_Hi= 0
    count_Low = 0
    for i in range(len(scores)-1):
        if Hi < scores[i+1]:
            Hi = scores[i+1]
            count_Hi+=1
        if Low > scores[i+1] :
            Low = scores[i+1]
            count_Low+=1       
    List_count =[count_Hi,count_Low]   
    return List_count      
            
            
        

if __name__=='__main__':
    scores =[3,4,21,36,10,28,35,5,24,42]
    print(breakingRecords(scores))
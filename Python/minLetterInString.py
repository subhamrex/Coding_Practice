#Question-> https://molchevskyi.medium.com/best-solutions-for-microsoft-interview-tasks-min-deletions-to-obtain-string-in-right-format-37a3365ce348
def solution(A):
    char_A = 'A' 
    num_Bs =0
    min_dels=0
    for c in A:
        if char_A ==c:
            min_dels = min(num_Bs, min_dels+1)
        else:
            num_Bs +=1
    return min_dels

if __name__ == '__main__':
    A = 'BBABAA'
    result =solution(A) 
    print(result)           
           
            
        
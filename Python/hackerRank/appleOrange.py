def countApplesAndOranges(s, t, a, b, apples, oranges):
    countA = 0
    countO = 0
    for i in range(len(apples)):
        apples[i] = apples[i] + a 
        if apples[i]>=s and apples[i]<=t:
            countA = countA + 1  
    print(countA)  
    for i in range(len(oranges)):
        oranges[i] = oranges[i] + b
        if oranges[i]>=s and oranges[i]<= t:
            countO += 1      
    print(countO)        
            


if __name__ == '__main__':
    # st = input().split()

    # s = int(st[0])

    # t = int(st[1])

    # ab = input().split()

    # a = int(ab[0])

    # b = int(ab[1])

    # mn = input().split()

    # m = int(mn[0])

    # n = int(mn[1])

    # apples = list(map(int, input().rstrip().split()))

    # oranges = list(map(int, input().rstrip().split()))
    s =7
    t = 10
    a = 4
    b = 12
    apples =[2,3,-4]
    oranges = [3,-2,-4]
    countApplesAndOranges(s, t, a, b, apples, oranges)
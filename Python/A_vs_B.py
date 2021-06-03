

def compareTriplets(a, b):
    Alice_P = 0
    Bob_P = 0
    List_P = [0, 0]
    for i in range(0, len(a)):
        if(a[i] > b[i]):
            Alice_P = Alice_P + 1
            List_P[0] = Alice_P
        if(a[i] < b[i]):
            Bob_P = Bob_P + 1
            List_P[1] = Bob_P

    return List_P


a = [17,28,30]

b = [99,16,8]

result = compareTriplets(a, b)
print(result)

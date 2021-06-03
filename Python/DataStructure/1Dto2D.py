resultList = [[None] * 3 for i in range(3)]
print(resultList)
for i in range(0,3):
    for j in range (0,3):
        resultList[i][j] = i + j
    print("my list: ",resultList[i]) 

print(resultList)

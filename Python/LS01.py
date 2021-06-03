# find the longest sequence of 1's by flipping 1 and 0.
arr = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
resultArr = []
sequenceTotal = 0
for i in range(len(arr)):
    if(arr[i] == 1):
        sequenceTotal += 1
        if(sequenceTotal > 0 and i == len(arr)-1):
            resultArr.append(sequenceTotal)
    else:
        if(sequenceTotal > 0):
            resultArr.append(sequenceTotal)
        resultArr.append(arr[i])
        sequenceTotal = 0
print(resultArr)
maxSquence = 0
for j in range(0, len(resultArr), 2):
    length = resultArr[j]
    if((j+1) < len(resultArr)):
        length += 1
    if((j+2) < len(resultArr)):
        length += resultArr[j+2]
    if(length > maxSquence):
        maxSquence = length
print(maxSquence)        

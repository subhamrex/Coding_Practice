def plusOne(digits):
    str1 = " "
    for ele in digits:
        str1 += str(ele)
    output = str(int(str1) + 1)
    for i in range(len(digits)):
        arr[i] = int(output[i])
    return digits

arr = [4,3,2,1]
print(plusOne(arr))
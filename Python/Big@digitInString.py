Mystring = "10101"
newString = ""
result =[]

for i in range(0, len(Mystring)-1):
    newString = newString + Mystring[i]+Mystring[i+1]
    result.append(int(newString))
    
    newString =""
print(max(result))    
list=[]
e=input("Enter string to encode:-")
d = input("Encoded String")
list =[e,d]
print("Do you want to encode or decode?")
user = input()
if(user=='e'):
    e=input("Enter string to encode:-")
    d = input("Encoded String")
    list =[e,d]
elif(user=='d'):
    print("Enter to Decoded:")
    a=input()
    if(a==list[1]):
        print("Decoded String: {list[1]}")

    

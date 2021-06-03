hello = open(r"C:\Users\SUBHAMREX\Desktop\VSCode_File\Python\hello2.txt",'w')
#print(hello.read())
#print(hello.readlines())
hello.write("Mr. Rex is here!!!\n")
hello.write("Mr. Rex is here2!!!")

hello.close()
#crete binary file
import shelve
shelfFile = shelve.open('mydata')
shelfFile['lang'] = ['c','c++','c#','java','python']
print(shelfFile['lang'])
shelfFile.close()
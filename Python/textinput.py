with open('textinputs.txt') as f:
    data = f.read().splitlines()

mylist1 = data[0].split() 
print(mylist1)
mylist1 = [int(x) for x in mylist1]
# mylist1 = list(map(int, mylist1))
print(mylist1[1])    
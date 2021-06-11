import array

a = array.array('i', [1, 2, 3])

# b = array.array('i', [1, 2, 'string'])    #OUTPUT: TypeError: an integer is required (got type str)

for i in a:
    print(i, end=' ') 

def Find_No(phnno):

    if len(phnno) != 10:
        return False
    for i in range(0, 10):
        if not no.isdecimal():
            return False
    return True


msg = "My Phone Numbers are 9800139449 and 7908428074"
foundNo = False
for i in range(len(msg)):
    no = msg[i:i+10]
    if Find_No(no):
        print(no)
        foundNo = True
if not foundNo:
    print("Not found")

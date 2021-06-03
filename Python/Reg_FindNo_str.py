import re

msg = "My Phone Numbers are 9800139449 and 7908428074"
NumReg = re.compile(r"\d\d\d\d\d\d\d\d\d\d")
Match_No = NumReg.findall(msg) # use search() for  first No
print(Match_No)

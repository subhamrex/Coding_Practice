import re
msg1 = "BatMan lost his BatMobile"
Reg_Num1 = re.compile(r"Bat(Man|Mobile)")
Match_OBJ1 = Reg_Num1.search(msg1)
print(Match_OBJ1.group())
print("----------------------------")
msg2 = "Batman cant fly"
msg3 = "Batwoman loves night"
Reg_Num2 = re.compile(r"Bat(wo)?man")
Match_OBJ2 = Reg_Num2.search(msg2)
Match_OBJ3 = Reg_Num2.search(msg3)
print(Match_OBJ2.group())
print(Match_OBJ3.group())
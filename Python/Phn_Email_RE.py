import re
import pyperclip
msg = 'phn no- +91 9800139449 and 09800139449 rex@gmail.com rexina_123@gmail.com'
phnRegex = re.compile(r'\+\d\d \d{10}|\d{11}')
resultPHnRegex = phnRegex.findall(msg)
#emailRegex = re.compile(r'[a-zA-Z0-9_.+]+@[a-zA-Z0-9_.+]+')
emailRegex = re.compile(r'\w+@\w+\.\w+')
resultemailRegex = emailRegex.findall(msg)

print(resultPHnRegex)
print(resultemailRegex)

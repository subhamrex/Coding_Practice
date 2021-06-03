def timeConversion(s):
    Arr_12H = list(map(str, [i + 1 for i in range(12)]))
    Arr_24H = list(map(str, [i + 13 for i in range(11)]))
    Arr_24H.append("00")
    if int(s[:2]) < 12 and s[-2:] == "AM":
        s = s[:(len(s)-2)]
    if int(s[:2]) < 12 and s[-2:] == "PM":
        s = s[:(len(s)-2)]
        for i in range(len(Arr_12H)):
            if int(s[:2]) == int(Arr_12H[i]):
                s = s[2:]
                s = Arr_24H[i] + s
                break
    if int(s[:2]) == 12 and s[-2:] == "AM":
        s = s[:(len(s)-2)]
        s = s[2:]
        s = "00" + s

    if int(s[:2]) == 12 and s[-2:] == "PM":
        s = s[:(len(s)-2)]

    print(s)


timeConversion("01:01:00PM")

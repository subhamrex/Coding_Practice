def birthdayCakeCandles(candles):
    maxcandle= max(candles)
    counter = 0
    for i in candles:
        if i==maxcandle:
            counter+=1
    return counter

arr =[4,4,1,3]
print(birthdayCakeCandles(arr))        
        
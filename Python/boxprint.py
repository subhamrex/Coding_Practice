def boxprint(symbol,width,height):
    if(len(symbol)!=1):
        raise Exception("symbol must be length of 1")
    print(symbol*width)
    for i in range(height - 2):
        print(symbol + " "*(width-2)+symbol)
    print(symbol*width)   
if __name__ == "__main__":
    boxprint('*',15,7)
    boxprint('x',15,7)   
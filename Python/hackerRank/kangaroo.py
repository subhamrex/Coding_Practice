def kangaroo(x1, v1, x2, v2):
    if v1>v2:
        while x1<x2:
            x1+=v1
            x2+=v2
    return "YES" if x1==x2 else "NO"    

if __name__ == "__main__":
    x1 =0
    v1=2
    x2 = 5
    v2 = 3
    
    result = kangaroo(x1, v1, x2, v2)
    print(result)

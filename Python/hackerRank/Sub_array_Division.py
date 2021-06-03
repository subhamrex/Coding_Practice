
def birthday(s, d, m):
    tp = (len(s)-m) + 1 #total number of pieces possible
    return len([1 for i in range(tp) if sum(s[i:i+m])==d])


if __name__ == '__main__':
    s = [5,1, 2, 4, 4, 2, 4, 2, 2, 5, 1, 4, 3, 1, 1, 1, 2, 1, 4, 1]
    d = 18
    m = 6
    print(birthday(s, d, m))
    #4

input1 = input()
input_list = list()
for i in range(int(input1)):
    n = input()
    input_list.append(n)

def solution(input_list):
    res_list = list()
    x = 20
    for i in range(len(input_list)):
        a1 = input_list[i].split(" ")
        a2 = [float(i) for i in a1]
        res = 40 * x+ (a2[0] - 40)*(x+a2[1])
        res_list.append(res)
    return res_list    



print(solution(input_list))
class Solution(object):
    def myAtoi(self, s):
        #Remove WhiteSpace
        s = s.strip()
        if (s == None or len(s) == 0):
            return 0
        res = 0
        isNeg = False
        start_index = 0
        
        if s[0] == '+' or s[0] == '-':
            start_index +=1
        
        if s[0] == '-':
            isNeg = True
        # Numeric case
        for i in range(start_index,len(s)):
            if ord(s[i]) < ord('0') or ord(s[i]) > ord('9'):
                break 
            digit_value = int(ord(s[i]) - ord('0'))
            res = res*10 + digit_value
          
        if(isNeg):
            res = -res
        min_value = pow(-2,31)
        max_value = (pow(2,31)-1)
        if (res < min_value):
            return min_value
        if (res > max_value):
            return max_value
        
        return int(res)
                      
if __name__ == '__main__':
    obj = Solution()  
    s = "-91283472332" 
    print(obj.myAtoi(s))     
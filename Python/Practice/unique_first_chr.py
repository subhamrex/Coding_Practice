class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        fre = {}
        for i in s:
            if i not in fre:
                fre[i] = 1
            else:
                fre[i] +=1
        for i in range(len(s)):
            if fre[s[i]] ==1:
                return i
        return -1    
if __name__ == '__main__':   
    obj = Solution() 
    s = "aabb" 
    print(obj.firstUniqChar(s)) 
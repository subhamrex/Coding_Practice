class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if len(matrix[-1]) ==0:
            return matrix
        res = []
        i_set = len(matrix) - 1
        i = i_set
        j = 0
        while (j < len(matrix[-1])):
            temp = []
            while(i >= 0):
                temp.append(matrix[i][j])
                i -=1
            res.append(temp)    
            i = i_set 
            j +=1 
        return res      
            
        
sol = Solution() 
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]   
print(f"Initial matrix: {matrix}")    
print(f"After rotation : {sol.rotate(matrix)}")

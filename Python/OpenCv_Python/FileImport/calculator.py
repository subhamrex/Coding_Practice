class Calculator():
    
    def add(self,x,y):
        res = "Error"
        if type(x) == int and type(y) == int:
            res = x + y
                
        return res
    
    def sub(self,x,y):
        res = "Error"
        if type(x) == int and type(y) == int:
            res = x - y
        
        return res    

    def mul(self,x,y):
        res = "Error"
        if type(x) == int and type(y) == int:
            res = x * y
        
        return res    
    
    def div(self,x,y):
        try:
            return  x / y
        
        except :
            return 'Error'
                
        


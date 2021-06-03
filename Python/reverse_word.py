# Write a program to reverse a word in a given string that is present in an input file.
# Enter input file = file.txt
# Enter line =  "Hello how are you?"
# Which word to reverse = 2
# Hello woh are you? 
# kavanan@telaverge.com
def reverse_word(S,SNo):
    SNo = SNo-1
    li = list(S.split(" "))
    if(SNo>len(li)-1 or SNo<1):
        return "Wrong Input"
    a = li[SNo]
    output=[]
    for i in range(len(a)-1,-1,-1):
        output.append(a[i])    
    Str1=''.join(str(ele) for ele in output)
    li[SNo]=Str1   
    Str2= ' '.join(str(ele) for ele in li)    
    return Str2
        
    
if __name__ == "__main__":
    with open("file.txt",'r') as f:
        myinput = f.read() # Here our Input from txt file is how are you?
    
        reverse_word_no = int(input("The word no we want to reverse:")) # Here we take 2 as a input
        print(reverse_word(myinput,reverse_word_no))
             
    
     
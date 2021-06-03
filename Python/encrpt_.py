# Given a string s, the task is to encrypt the string in the following way:

# If the frequency of current character is even, then increment current character by x.
# If the frequency of current character is odd, then decrement current character by x.
# Python3 implementation of the above approach: 
MAX = 26
  
# Function to return the encrypted strring 
def encryptstrr(strr, n, x): 
      
    # Reduce x because rotation of 
    # length 26 is unnecessary 
    x = x % MAX
    arr = list(strr) 
      
    # calculate the frequency of characters 
    freq = [0]*MAX
    for i in range(n): 
        freq[ord(arr[i]) - ord('a')] += 1
      
    for i in range(n): 
          
        # If the frequency of current character 
        # is even then increment it by x 
        if (freq[ord(arr[i]) - ord('a')] % 2 == 0): 
            pos = (ord(arr[i]) - ord('a') + x) % MAX
            arr[i] = chr(pos + ord('a')) 
          
        # Else decrement it by x 
        else: 
            pos = (ord(arr[i]) - ord('a') - x) 
            if (pos < 0): 
                pos += MAX
            arr[i] = chr(pos + ord('a')) 
              
    # Return the count 
    return "".join(arr) 
  
  
# Driver code 
s = "abcda"
n = len(s) 
x = 3
print(encryptstrr(s, n, x)) 
    
    

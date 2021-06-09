package Java_Practice;
public class substringOfString {
    static int issubstring(String A,String B) 
    {
        int LenA = A.length();
        int LenB = B.length();
        for(int i = 0; i <(LenA - LenB)+1;i++ )
        {   int j;
            for( j = 0; j<LenB;j++)
            {
                if(A.charAt(i+j) != B.charAt(j))
                {
                    break;
                }


            }
            
            if(j == LenB)
            {
                return i;
            }
        }
        return -1;
    }
    public static void main(String[] args) {
        String A = "KaliRexHacky";
        String B = "Rexx";
        int result =issubstring(A, B);

        if(result == -1)
        { 
            System.out.println("Not a Substring");

        }
        else{
            System.out.println("Given String is a Substring");

        }
        
       
        
        
    }
    
    
}

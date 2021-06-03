public class print_count{
      
    
    static boolean isPrime(int n)
    {
        if (n <= 1)
            return false;
      
        for (int i = 2; i <= Math.sqrt(n); i++) {
            if (n % i == 0)
                return false;
        }
      
        return true;
    }
      
   
    static boolean isPossible(int N)
    {
       
        if (isPrime(N) && isPrime(N - 2))
            return true;
        else
            return false;
    }
      
     
     public static void main(String args[]){
           
        for (int i=0;i<args.length;i++){

       if (isPossible(args[i]) == true)
            System.out.println("Yes");
        else
            System.out.println("No");
}
	
          
      
        
     }
    
}
import java.util.Scanner;
import java.util.Random;
public class SeqString{
    public static String toString(char[] a) 
    { 
        String string = new String(a); 
        if(string.endsWith(".")==true)
        {
            string= string.replace(".","");
        }
        return string; 
    }
    public static void main(String[] args){
        Scanner myObj = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = myObj.nextLine(); 
        System.out.print("\nInput: ");
        char chr = myObj.next().charAt(0);
        char symbols[] = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/'};
        Random rand = new Random();
        int ranInt = rand.nextInt(symbols.length); 

        char string[] = str.toCharArray();
        int count = 0;
        myObj.close();

        for (int i=0;i<str.length();i++)
        {
            if(string[i]== chr)
            {
                count++;
            }
            
            if(string[i] ==' ' && Character.isLowerCase(string[i+1])==true && (i+1) <str.length())
            {
                string[i+1] =  Character.toUpperCase(string[i+1]);
            }
           
            
            
        }
            
        System.out.println("Output: ");
        System.out.println("Frequency of "+chr+" = "+ count );
        System.out.println("Final string: "+toString(string)+" "+ symbols[ranInt]+".");




        
    }
}
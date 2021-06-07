import java.util.Scanner;
public class chrNo {
    public static void main(String[] args)
    {
    //97 lower 65 upper
        Scanner myObj = new Scanner(System.in);
        System.out.print("Input: ");
        String str = myObj.nextLine(); 
        System.out.print("\nstring to be replaced: ");
        String str2 = myObj.nextLine();
        System.out.print("\nstring to be replaced with: ");
        String str3 = myObj.nextLine();
        String StringRes[] = new String[10];
        myObj.close();

        String RepStr = str.replace(str2, str3);
        char string[] = str3.toCharArray();
        for (int i=0; i<str3.length(); i++)
        {
           if(Character.isUpperCase(string[i])==true)
        {   int res = string[i];
            int result = (res -65)+1;
            String Res= Integer.toString(result);
            StringRes[i]=Res;
        }
        if(Character.isLowerCase(string[i])==true)
        {   int res = string[i];
            int result = (res-97)+1;
            String Res= Integer.toString(result);
            StringRes[i]=Res;
        }
        }
        System.out.print("\noutput: "+RepStr+" ");
        for (int i=0;StringRes[i]!=null;i++)
        {
            System.out.print(StringRes[i]);
        }
        
    }
}

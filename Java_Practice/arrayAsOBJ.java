package Java_Practice;
class objArray{
  String name;
  int age;
  public objArray(String name, int age)
  {
      this.name = name;
      this.age = age;
  }
}
public class arrayAsOBJ {
    public static void main(String[] args) {
        objArray[] newArray = new objArray[3];
        newArray[0] = new objArray("Rex",7);
        newArray[1] = new objArray("Kali",0);
        newArray[2] = new objArray("Hacky",1);
        for (int i = 0;i<newArray.length;i++)
        {
            System.out.println(newArray[i].name);
        }


        
    }
    
}

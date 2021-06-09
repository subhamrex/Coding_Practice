package Java_Practice;



public class spiralMatrix {
    void printspiral(int [][] arr)
    {
       int first_row = 0;  
       int last_row = arr.length-1;
       int first_col = 0;
       int last_col = arr[0].length-1;
       while(first_row < last_row && first_col < last_col)
       {
            //up
            for(int i = first_col; i <=last_col; i++)
            {
                System.out.println(arr[first_row][i]);
            }
            for(int i = first_row+1; i <= last_row; i++)
            {
                System.out.println(arr[i][last_col]);
            }
            for(int i = last_col; i>=first_col ; i--)
            {
                System.out.println(arr[last_row][i]);
            }
            for(int i=last_row-1; i>first_row;i--)
            {
                System.out.println(arr[i][first_col]);
            }

           first_row++;
           last_row--;
           first_col++;
           last_col--;
       }
    }

    public static void main(String[] args) {
        int [][] arr= {{1,1,1,2},
                       {4,5,5,2},
                       {4,6,5,2},
                       {4,3,3,3}};
       new spiralMatrix().printspiral(arr);
    
      

}
}

import java.util.*;

public class Main {
    public static void main(String[] args) {
      
   
     Scanner sc=new Scanner(System.in);
     int x=sc.nextInt();
     int n=0;
     int count =0;
     while(count<x-1)
     {
        if(n%2!=0)
        {
          System.out.print(n+",");
          count++;
        }
        n++;
     }
     System.out.print(n+1);
    
  }
}

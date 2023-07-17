package mypropose1;

import java.util.Scanner;
class Cal{
	public static void main(String[]  args) {
		
		Scanner sc=new Scanner(System.in);
		int input=sc.nextInt();
		int count=1;
		int i;
		
		
		for (i=1;count<input;i+=2){
			System.out.print(i+",");
		  count++;
		}
		System.out.print(i);
	}
}

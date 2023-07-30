package com.example.SK;
import java.util.Scanner;
public class Array_sum {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the Size of the Array : ");
		int a=sc.nextInt();
		int[] t=new int[a];
		for(int i=0;i<a;i++) {
			t[i]=sc.nextInt();
		}
		int sum=0,mul=1;
		for(int j:t) {
			sum+=j;
			mul*=j;
		}
		int A=(sum%2==0)?sum:mul;
		System.out.println(A);

	}

}

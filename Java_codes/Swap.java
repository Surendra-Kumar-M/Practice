package com.example.SK;

import java.util.Scanner;

public class Swap {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the first Number :");
		int N1=sc.nextInt();
		System.out.println("Enter the Second Number :");
		int N2=sc.nextInt();
		N1=N1+N2;
		N2=N1-N2;
		N1=N1-N2;
		System.out.println("The first Number : "+N1);
		System.out.println("The Second Number : "+N2);
		
	}

}

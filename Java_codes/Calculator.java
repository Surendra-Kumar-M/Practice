package com.example.SK;

import java.util.Scanner;

public class Calculator {

	static int add(int a, int b) {
		return a+b;
	}
	static int sub(int a, int b) {
		return a-b;
	}
	static double mul(int a, int b) {
		return a*b;
	}
	static float div(int a, int b) {
		return a/b;
	}
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the Number : ");
		int x=sc.nextInt();
		System.out.print("Enter the Number : ");
		int y=sc.nextInt();
		System.out.println("Addition : "+add(x,y));
		System.out.println("Subtraction : "+sub(x,y));
		System.out.println("Multiplication : "+mul(x,y));
		System.out.println("Division : "+div(x,y));

	}

}

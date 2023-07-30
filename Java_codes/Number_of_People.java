package com.example.SK;

import java.util.Scanner;

public class Number_of_People {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Total Number of People :");
		int t=sc.nextInt();
		double a=(t/3.5);
		System.out.println("Number of People on Day 1: "+(int)(a));
		System.out.println("Number of People on Day 2: "+(int)(2*a));
		System.out.println("Number of People on Day 3: "+(int)(a/2));
		
		

	}

}

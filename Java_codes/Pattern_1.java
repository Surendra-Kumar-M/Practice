package com.example.SK;

import java.util.Scanner;

public class Pattern_1 {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Number");
		int a=sc.nextInt();
		for(int i=0;i<a;i++) {
			for(int j=a-i;j>i;j--) {
				System.out.print(" ");
			}
			for(int k=0;k<=i;k++) {
				System.out.print(" * ");
			}
			System.out.println();	
	}
	}
}

package com.example.SK;

import java.util.Scanner;

public class Concat {
	static String con(String s1,String s2) {
		return s1+s2;
	}
	static String con(String s1,String s2,String s3) {
		return s1+s2+s3;
	}

	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		System.out.print("Enter the string : ");
		String a=sc.nextLine();
		System.out.print("Enter the string : ");
		String b=sc.nextLine();
		System.out.print("Enter the string : ");
		String c=sc.nextLine();
		System.out.println(con(a,b));
		System.out.println(con(a,b,c));
		
	}

}

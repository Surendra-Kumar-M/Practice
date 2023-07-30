package com.example.SK;

import java.util.Scanner;

public class Reverse {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the String :");
		String a=sc.nextLine();
		char[]n=a.toCharArray();
		String rev="";
		for(int i=a.length()-1;i>=0;i--) {
			rev+=n[i];
		}
		System.out.println("Reversed String : "+rev);

	}

}

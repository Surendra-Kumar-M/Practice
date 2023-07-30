package com.example.SK;

import java.util.Scanner;

public class Palindrome {

	public static void main(String[] args) {
		String a,b="";
		Scanner s= new Scanner(System.in);
		System.out.print("Enter a String : ");
		a=s.nextLine();
		for(int i=a.length()-1;i>=0;i--) {
			b+=a.charAt(i);
		}
		if(a.equalsIgnoreCase(b))
			System.out.print("The Given String is Palindrome");
		else
			System.out.print("The Given String is not a Palindrome");
		
	}

}

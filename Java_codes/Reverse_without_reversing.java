package com.example.SK;

import java.util.Scanner;

public class Reverse_without_reversing {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the String : ");
		String c="",a=sc.nextLine();
		String[] b=a.split("\\s+"); 
		for(int i=b.length-1;i>=0;i--) {
			c+=b[i]+" ";
		}
		System.out.println(c);
		}
		
	}


package com.example.SK;

import java.util.Scanner;

public class GCD {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter First Number :");
		int a=sc.nextInt();
		System.out.println("Enter Second Number :");
		int b=sc.nextInt();
		int i=Math.min(a, b);
		int n=0;
		for(int j=i;j>=1;j--) {
			if(((a%j)==0)&&((b%j)==0)) {
				n=j;
				break;
			}
			}
		System.out.println("The Greatest Common Divisor of "+a+" and "+b+" is "+n);
	}

}

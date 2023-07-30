package com.example.SK;

import java.util.Scanner;

public class Cards {

	public static void main(String[] args) {
		int a,b,c;
		char A,B,C;
		Scanner sc=new Scanner(System.in);
		A=sc.next().charAt(0);
		a=sc.nextInt();
		B=sc.next().charAt(0);
		b=sc.nextInt();
		C=sc.next().charAt(0);
		c=sc.nextInt();
		if(((a==b)&&(b==c)) && ((A==B)&&(B==C))) {
			System.out.println("Double Bonanza");
		}
		else if((a==b)&&(b==c)) {
			System.out.println("Bonanza");
		}
		else {
			System.out.println("No Bonanza");
		}
	}
}


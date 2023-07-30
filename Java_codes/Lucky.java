package com.example.SK;

import java.util.Scanner;

public class Lucky {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Ticket Number");
		long a=sc.nextLong();
		if(a%10==3 || a%10==8)
			System.out.print("Lucky Winner");
		else
			System.out.print("Better Luck Next Time");

	}

}

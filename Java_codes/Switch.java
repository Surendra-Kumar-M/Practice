package com.example.SK;

import java.util.Scanner;

public class Switch {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		System.out.print("");
		int a=sc.nextInt();
		switch(a) {
		case 1:
			System.out.println("From 1");
			break;
		case 2:
			System.out.println("From 2");
			break;
		case 3:
			System.out.println("From 3");
			break;
		default:
			System.out.println("From Default");
		}
	}

}

package com.example.SK;

import java.util.Scanner;

public class Methods {

	public static void Lusu() {
		System.out.println("Hello Thangam");
	}
	public static void main(String[] args) {
		Lusu();
		Scanner sc=new Scanner(System.in);
		System.out.print("Enter the Name : ");
		String a=sc.nextLine();
		Love(a);
		System.out.print(a);

	}
	public static String Love(String s) {
		System.out.println("Love you Mental");
		return s;
	}

}

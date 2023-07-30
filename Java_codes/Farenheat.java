package com.example.SK;

import java.util.Scanner;

public class Farenheat {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Celcius :");
		double C=sc.nextInt();
		double F=1.8*C+32;
		System.out.println("The Celcius :"+C+" is equal to "+F+" Farenheat");

	}

}

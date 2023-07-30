package com.example.SK;

import java.util.Scanner;

public class Area_of_Polygon {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Number of Sides of the Polygon :");
		double n=sc.nextDouble();
		System.out.println("Enter the Length of a side :");
		double s=sc.nextDouble();
		double a;
		a=((n*s*s)/(4*Math.tan(Math.PI/n)));
		System.out.println("The Area is :"+a);

	}

}

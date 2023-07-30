package com.example.SK;

import java.text.DecimalFormat;
import java.util.Scanner;


public class Area_of_Equilateral_Triangle {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		DecimalFormat d=new DecimalFormat("0.00");
		System.out.println("Enter the Side of the Triangle :");
		int a=sc.nextInt();
		double t=(Math.sqrt(3)/4)*(a*a);
		System.out.println("The area of the Equilateral triangle is :"+(d.format(t)));

	}

}

package com.example.SK;

import java.text.DecimalFormat;
import java.util.Scanner;

public class Percentage {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		DecimalFormat d=new DecimalFormat("0.00");
		double b,t,f,l;
		b=sc.nextDouble();
		t=sc.nextDouble();
		f=sc.nextDouble();
		l=sc.nextDouble();
		double sum=b+t+f+l;
		System.out.println("Total expense : Rs."+sum);
		System.out.println("Brand percentage"+d.format(((b/sum)*100))+"%");
		System.out.println("Travel percentage"+d.format(((b/sum)*100))+"%");
		System.out.println("Food percentage"+d.format(((b/sum)*100))+"%");
		System.out.println("Logistics percentage"+d.format(((b/sum)*100))+"%");
	}
}	




	



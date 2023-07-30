package com.example.SK;

import java.util.Scanner;

public class count_the_occurance_of_letters {

	public static void main(String[] args) {
	
		Scanner sc=new Scanner(System.in);
		String a=sc.next();
		char[] h= {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
		int[] k= {};
		char[] m= {};
		
		for(int i=0;i<a.length();i++) {
			int count=1;
				
			for(int j=1;j<a.length();j++){
				if(a.charAt(i)==(a.charAt(j))) {
					count++;
				}
				
			}
			System.out.println(a.charAt(i)+" "+count);
		}
		StringBuffer b=new StringBuffer(a);
	}

}

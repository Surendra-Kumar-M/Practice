package com.example.SK;
import java.util.Scanner;
public class Mavintec {
  	public static void main(String[] args) {
		Scanner sc =new Scanner(System.in);
		String s=sc.nextLine();
		int rChar=0;
		int strlen=s.length();
		char arr[]=s.toCharArray();
		for(int i=0;i<strlen;i++) {
			int count=0;
			for(int j=(i+1);j<strlen;j++)
			{
				if(arr[i]==arr[j])
				{
					count++;
					for(int k=j;k<(strlen-1);k++)
						arr[k] = arr[k+1];
					strlen--;
					j--;
				}
			}
			if(count>0)
				rChar++;
		}
		System.out.println(rChar);
	}

}
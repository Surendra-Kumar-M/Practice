package com.example.SK;

public class Overloading {

	static int add(int a) {
		return a;
	}
	static int add(int a,int b) {
		int d=a+b;
		return d;
	}
	static float add(float a,float b) {
		float d=a+b;
		return d;
	}
	public static void main(String[] args) {
		System.out.println(add(10));
		System.out.println(add(10,20));
		System.out.println(add(10.0f,20.0f));
		System.out.println(add(100));

	}

}

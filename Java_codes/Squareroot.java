import java.util.Scanner;
import java.lang.Math;
class Squareroot{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
double num=s.nextDouble();
if(num>=0){
double b=Math.sqrt(num);
System.out.println("Square Root of "+num+" = "+b);
}
else{
System.out.println("Enter a Positive integer Number");
}
}
}
import java.util.Scanner;
class Odd_or_Even
{
public static void main(String args[]){
Scanner sc=new Scanner(System.in);
int a,b;
System.out.println("Enter a Number");
a=sc.nextInt();
if(a%2==0){
System.out.println("Number "+a+" is Even");
}
else{
System.out.println("Number "+a+" is Odd");
}
}}
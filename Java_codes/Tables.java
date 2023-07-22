import java.util.Scanner;
class Tables
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int a=s.nextInt();
for(int i=1;i<=20;i++){
System.out.println(i+" X "+a+" = "+i*a);
}
}                                                  
}
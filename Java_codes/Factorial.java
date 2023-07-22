import java.util.Scanner;
class Factorial
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter the Number");
long a=s.nextLong();
long f=1;
for(long i=1;i<=a;i++){
f*=i;
}
System.out.println("The Factorial of "+a+" is "+f);
}                                                  
}
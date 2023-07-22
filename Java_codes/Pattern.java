import java.util.Scanner;
class Pattern
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Symbol");
String b=s.next();
System.out.println("Enter a Number");
int a=s.nextInt();
for(int i=1;i<=a;i++){
System.out.println(b.repeat(i));
}
}                                                  
}
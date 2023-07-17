import java.util.Scanner;
class Do_While
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter Your Name");
String b=s.nextLine();
System.out.println("Enter a Number");
int a=s.nextInt();
int n=1;
do{
System.out.println(b);
n++;
}
while(a>=n);
}                                                  
}
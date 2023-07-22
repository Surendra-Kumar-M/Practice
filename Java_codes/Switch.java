import java.util.Scanner;
class Switch
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int b=s.nextInt();
switch(b%2){
case 0:
System.out.println("Number is Even");
break;
case 1:
System.out.println("Number is ODD");
break;
}
}                                                  
}
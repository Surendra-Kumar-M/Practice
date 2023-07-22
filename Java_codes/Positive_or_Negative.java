import java.util.Scanner;
class Positive_or_Negative
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int a=s.nextInt();
if(a>=0){
System.out.println(a+" is Positive ");
}
else{
System.out.println(a+" is Negative ");
}
}                                                  
}
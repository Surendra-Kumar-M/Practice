import java.util.Scanner;
class Greatest_Number{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int a=s.nextInt();
System.out.println("Enter a Number");
int b=s.nextInt();
if(a>b){
System.out.println("Number "+a+" is Greater than "+b);
}
else{
System.out.println("Number "+b+" is Greater than "+a);
}
}
}
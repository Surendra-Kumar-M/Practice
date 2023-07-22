import java.util.Scanner;
class Sum_of_Natural_Numbers{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int num=s.nextInt();
if(num>0){
int b=num*(num+1)/2;
System.out.println("Sum of "+num+" Natural Numbers ="+b);
}
else{
System.out.println("It's Not a Natural Number");
}
}
}
import java.util.Scanner;
class Natural_Numbers
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int a=s.nextInt();
if(a>0){
System.out.println(a+" is a Natural Number ");
}
else{
System.out.println(a+" is Not a Natural Number ");
}
}                                                  
}
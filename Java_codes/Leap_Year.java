import java.util.Scanner;
class Leap_Year{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Year");
int year=s.nextInt();
if(year%4==0){
System.out.println(year+" is a Leap Year");
}
else{
System.out.println(year+" is Not a Leap Year");
}
}
}
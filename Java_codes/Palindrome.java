import java.util.Scanner;
class Palindrome
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int n=s.nextInt();
int r,sum=0,temp;
temp=n;
while(n>0){
r=n%10;
sum=(sum*10)+r;
n=n/10;
}
if(temp==sum){
System.out.println("It is Palindrone");
}
else{
System.out.println("It is not a Palindrone");
}
}                                                  
}
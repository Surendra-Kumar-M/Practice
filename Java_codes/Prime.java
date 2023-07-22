import java.util.Scanner;
class Prime{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter a Number");
int a=s.nextInt();
boolean b=false;
for(int i=2;i<=a/2;i++){
if(a%i==0){
b=true;
}
}
if(!b){
System.out.println("Number "+a+" is Prime");
}
else{
System.out.println("Number "+a+" is Not Prime ");
}
}
}
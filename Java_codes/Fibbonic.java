import java.util.Scanner;
class Fibbonic
{
public static void main(String args[]){
Scanner s=new Scanner(System.in);
System.out.println("Enter the Number of Fibbonic Seies Required");
int a=s.nextInt();
System.out.println("Fibbonic Series");
int f=0;
int g=1;
for(int i=1;i<=a;i++){
if(f<=a){
System.out.println(f);
f=f+g;
g=f-g;
}
}
}                                                  
}
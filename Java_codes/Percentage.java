import java.text.DecimalFormat;
import java.util.Scanner;
public class Percentage {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		DecimalFormat d=new DecimalFormat("0.00");
		double b,t,f,l;
		b=sc.nextDouble();
		t=sc.nextDouble();
		f=sc.nextDouble();
		l=sc.nextDouble();
		double sum=b+t+f+l;
		System.out.println("Brand Percentage "+d.format(((b/sum)*100))+"%");
		System.out.println("Travel Percentage "+d.format(((t/sum)*100))+"%");
		System.out.println("Food Percentage "+d.format(((f/sum)*100))+"%");
		System.out.println("Logistics Percentage " +d.format((l/sum)*100)+"%");
	}

}
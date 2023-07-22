import java.util.Scanner;
public class Time {
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter the Minutes :");
		int a=sc.nextInt();
		double day;
		day=a/(60*24);
		System.out.println("Days: "+(float)day);
		double year;
		year=day/(365.25);
		System.out.println("Years: "+(float)year);
	
		
	}

}

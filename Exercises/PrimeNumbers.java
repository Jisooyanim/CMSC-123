import java.util.Scanner;
import java.lang.Math;


public class PrimeNumbers {
	
	public static void solution(int N) {
		for(int i = 2; i <= N; i++){//Loops until N
			boolean prime = true;
			for(int j = 2; j <= Math.sqrt(i); j++){//Find factors
				if(i % j == 0){
					prime = false;//There is a factor
				}
			}
			if(prime == true)
				System.out.print(i + " ");
		}
	}

	public static void main(String[] args) {

		Scanner input = new Scanner(System.in);
		System.out.print("Enter N: ");
		int n = input.nextInt();
		solution(n);
		input.close();
	}
}
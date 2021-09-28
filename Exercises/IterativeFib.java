import java.util.Scanner; 
import java.math.BigInteger;

public class IterativeFib {

	public static void iterativeFib(int N) {
		BigInteger term_0 = BigInteger.valueOf(0);//The zeroth term = 0
		BigInteger term_1 = BigInteger.valueOf(1);//The first term = 1
		BigInteger ans = BigInteger.valueOf(0);//The resulting answer

		if(N == 0)
			System.out.println(term_0);
		else if(N == 1)
			System.out.println(term_1);
		else
			for(int i = 0; i < N - 1; i++){
				ans = term_0.add(term_1);
				term_0 = term_1;
				term_1 = ans;
			}
			System.out.println(ans);
	}
	
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.print("Enter N: ");
		int N = input.nextInt();
		iterativeFib(N);
		input.close();
	}
}
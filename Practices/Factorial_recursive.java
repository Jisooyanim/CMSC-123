import java.util.Scanner;

public class Factorial_recursive {
    public static long factorial(int N){
        if(N == 0 || N == 1)
            return 1;
        if(N < 1)
            return -1;
        return N * factorial(N - 1);
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter N: ");
        int input = scanner.nextInt();
        System.out.println(factorial(input));

        scanner.close();
    }
}
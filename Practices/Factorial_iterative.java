import java.util.Scanner;

public class Factorial_iterative {
    public static long factorial(int N){
        int i = 0;
        int fact = 1;

        while(i < N){
            i++;
            fact *= i;
        }

        return fact;
    }
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter N: ");
        int input = scanner.nextInt();
        System.out.println(factorial(input));

        scanner.close();
    }    
}
import java.util.Scanner;

public class Smallest_element{
    public static int indexSmallestElement(double[] L){
        int n = L.length;
        int indexMin = 0;

        for(int i = 1; i < n; i++){
            if(L[indexMin] > L[i]){
                indexMin = i;
            }
        }

        return indexMin;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the size of the list: ");
        int input = scanner.nextInt();

        double[] list = new double[input];
        for(int i = 0; i < input; i++){
            list[i] = scanner.nextDouble();
        }
        scanner.close();

        System.out.print("Index of smallest element is: ");
        System.out.print(indexSmallestElement(list));
    }
}
package lab6;
import java.util.Scanner;

public class Lab06_Q2 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please input the natural number: ");
        int number = in.nextInt();

        int sum = primeSummation(number);
        System.out.println("The summation of the prime factors of " + number + " is " + sum + ".");

        in.close();
    }

    public static boolean isPrime(int input) {
        boolean prime = true;
        for (int i = 2; i < input; i++) {
            if (input % i == 0) {
                prime = false;
            }
        }
        return prime;
    }

    public static int primeSummation(int input) {
        int sum = 0;
        for (int i = 2; i <= input; i++) {
            if (input % i == 0 && isPrime(i)) {
                sum += i;
            }
        }
        return sum;
    }
}

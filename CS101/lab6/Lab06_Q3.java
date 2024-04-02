package lab6;
import java.util.Scanner;

public class Lab06_Q3 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please input the first number: ");
        int a = in.nextInt();
        System.out.print("Please input the second number: ");
        int b = in.nextInt();
        System.out.print("Please input the third number: ");
        int c = in.nextInt();

        if (!isPythagorean(a, b, c)) {
            System.out.println("The triplet is not Pythagorean.");
        }

        in.close();
    }

    public static int power(int base, int power) {
        int result = 1;
        for (int i = 0; i < power; i++) {
            result = result * base;
        }
        return result;
    }

    public static boolean isPythagorean(int a, int b, int c) {
        int total = power( a, 2) + power( b, 2) + power( c, 2);
        boolean pythagorean = false;

        if (a > b && a > c) {
            if (2 * power( a, 2) == total) {
                pythagorean = true;
                System.out.printf("The triplet is Pythagorean, power(%d, 2) = power(%d ,2) + power(%d ,2)%n", a, c, b);
            }
        }
        else if (b > a && b > c) {
            if (2 * power( b, 2) == total) {
                pythagorean = true;
                System.out.printf("The triplet is Pythagorean, power(%d, 2) = power(%d ,2) + power(%d ,2)%n", b, a, c);
            }
        }
        else if (c > a && c > b) {
            if (2 * power( c, 2) == total) {
                pythagorean = true;
                System.out.printf("The triplet is Pythagorean, power(%d, 2) = power(%d ,2) + power(%d ,2)%n", c, a, b);
            }
        }
        return pythagorean;

    }
}

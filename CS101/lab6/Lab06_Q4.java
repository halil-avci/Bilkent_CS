package lab6;
import java.util.Scanner;

public class Lab06_Q4 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please enter the first natural number: ");
        int num1 = in.nextInt();
        System.out.print("Please enter the second natural number: ");
        int num2 = in.nextInt();

        System.out.println("Binary representation of the first number: " + intToBinary(num1));
        System.out.println("Binary representation of the second number: " + intToBinary(num2));
        System.out.println("The bitwise AND operation result: " + binaryAND(num1, num2));
        System.out.println("The bitwise OR operation result: " + binaryOR(num1, num2));

        in.close();
    }

    public static long intToBinary(int input) {
        long binary = 0;
        int count = 0;
        int inputCopy = input;

        while (inputCopy != 0) {
            int remainder = inputCopy % 2;
            if (remainder == 1) {
                binary += (int) Math.pow( 10, count);
            }

            inputCopy = inputCopy / 2;
            count++;
        }
        return binary;
    }

    public static long binaryAND(int in1, int in2) {
        long binary1 = intToBinary(in1);
        long binary2 = intToBinary(in2);
        long result = 0;
        int count = 0;

        while (binary1 > 0 && binary2 > 0) {
            if (binary1 % 10 == 1 && binary2 % 10 == 1) {
                result += (int) Math.pow( 10, count);
            }
            binary1 = binary1 / 10;
            binary2 = binary2 / 10;
            count++;
        }
        return result;
    }

    public static long binaryOR(int in1, int in2) {
        long binary1 = intToBinary(in1);
        long binary2 = intToBinary(in2);
        long result = 0;
        int count = 0;

        while (binary1 > 0 && binary2 > 0) {
            if (binary1 % 10 == 1 || binary2 % 10 == 1) {
                result += (int) Math.pow( 10, count);
            }
            binary1 = binary1 / 10;
            binary2 = binary2 / 10;
            count++;
        }
        return result;
    }
}

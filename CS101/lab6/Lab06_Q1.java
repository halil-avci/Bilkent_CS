package lab6;
import java.util.Scanner;

public class Lab06_Q1 {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Please input the password: ");
        int password = in.nextInt();

        int decoded = passwordDecoder( password);
        System.out.println("The decoded password is: " + decoded);

        in.close();
    }

    public static int floor(double number) {
        return (int) number;
    }

    public static int digitDecoder(int digit) {
        double doubleDigit = digit;
        int decodedDigit = floor( 10 - Math.pow( doubleDigit / 2 - 3, 2) - 0.32);
        return decodedDigit;
    }

    public static int passwordDecoder(int input) {

        int decodedPassword = 0;
        int counter = 0;
        
        while (input > 0) {
            int lastDigit = input % 10;
            decodedPassword += digitDecoder( lastDigit) * Math.pow( 10, counter);

            input = input / 10;
            counter++;
        }

        return decodedPassword;
    }
}

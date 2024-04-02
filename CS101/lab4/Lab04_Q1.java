package lab4;

/**
 * Lab04_Q1
 * 
 * This program takes a positive integer from user,
 * inverts and prints it.
 */

import java.util.Scanner;

public class Lab04_Q1 {
    public static void main(String[] args) {
        //Take input from user
        Scanner in = new Scanner( System.in);
        System.out.print( "Enter input n: ");
        
        //Check if the input is a positive integer
        if (in.hasNextInt()) {
            int n = in.nextInt();

            if (n > 0) {
                int inverted = 0;

                //Find digit number
                int length = (int) (Math.log10(n) + 1);

                //Invert the positive integer
                while (n != 0) {
                    int lastDigit = n % 10;
                    inverted = (int) (inverted + lastDigit * Math.pow( 10, length - 1));
                    length--;
                    n = n / 10;
                }
                //Print the inverted number
                System.out.println( inverted);
            }
            else {
                System.out.println( "Please enter a positive integer!");
            }
        }
        else {
            System.out.println( "Input is not a number!");
        }
        in.close();
    }
}
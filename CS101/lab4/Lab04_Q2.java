package lab4;

/**
 * Lab04_Q2
 * 
 * This program takes an integer from user, converts it to binary,
 * stores it as an integer and prints it out.
 */

import java.util.Scanner;

public class Lab04_Q2 {
    public static void main(String[] args) {
        Scanner in = new Scanner( System.in);
        System.out.print( "Please input n: ");
        int n = in.nextInt();

        int binary = 0;
        int counter = 0;

        while (n != 0) {
            int remainder = n % 2;
            
            if (remainder == 1) {
                binary = binary + (int) Math.pow( 10, counter);
            }

            n = n / 2;
            counter++;
        }

        System.out.println( binary);
        in.close();
    }
}
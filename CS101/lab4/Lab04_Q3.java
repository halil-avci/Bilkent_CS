package lab4;

/**
 * Lab04_Q3
 * 
 * This program gets input from the user, converts it to binary number,
 * does the asked operation and prints it.
 * 
 */

import java.util.Scanner;

public class Lab04_Q3 {
    public static void main(String[] args) {
        Scanner in = new Scanner( System.in);
        String answer = "y";
        
        while (answer.equals( "y")) {
            //Get input from user
            System.out.print( "Enter input n: ");
            int n = in.nextInt();

            //Convert input to binary
            int binary = 0;
            int count = 0;

            while (n != 0) {
                int remainder = n % 2;
                
                if (remainder == 1) {
                    binary = binary + (int) Math.pow( 10, count);
                }

                n = n / 2;
                count++;
            }

            //Get the operation and multiplier or divisior from user
            System.out.print( "Please choose the operation. Division or Multiplication 'd' or 'm'?: ");
            String operation = in.next();
            System.out.print( "Enter the multiplier or divisor that is a multiple of two: ");
            int operationNumber = in.nextInt();

            //Find how many shifts are needed
            int shifting = 0;
            while (operationNumber != 1) {
                operationNumber = operationNumber / 2;
                shifting++;
            }

            //Multiply the binary number according to shifting variable
            if (operation.equals("m")) {
                String result = "0b" + binary * (int) Math.pow( 10, shifting);
                System.out.println( result);
            }
            //Divide the binary number according to shifting variable
            else {
                String result = "0b" + binary / (int) Math.pow( 10, shifting);
                System.out.println( result);
            }
            
            //Ask if the user wants to continue
            System.out.print( "Do you want to do another operation? 'y' (yes) or 'n' (no): ");
            answer = in.next();
            System.out.println();
        }

        //Finish the program
        System.out.println( "Program finished.");
        in.close();
    }
}
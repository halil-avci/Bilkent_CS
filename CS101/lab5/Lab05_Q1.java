package lab5;

import java.util.Scanner;

public class Lab05_Q1 {
    public static void main(String[] args) {
        //Get input
        Scanner in = new Scanner( System.in);
        System.out.printf( "Please enter 'falling stars' as string: ");
        String input = in.next();

        System.out.println( "Falling stars:");
        System.out.println( input);

        //Get the biggest number in the string
        int biggestNumber = 0;
        for (int i = 0; i < input.length(); i++) {
            if (Integer.parseInt( input.substring( i, i + 1)) > biggestNumber){
                biggestNumber = Integer.parseInt( input.substring( i, i + 1));
            }
        }

        //Print the stars
        for (int line = 0; line < biggestNumber; line++) {
            for (int digit = 0; digit < input.length(); digit++) {
                String number = input.substring( digit, digit + 1);
                int intNumber = Integer.parseInt( number);

                if (intNumber - line > 0) {
                    System.out.print( "*");
                }
                else {
                    System.out.print( " ");
                }
            }
            System.out.println();
        }
        in.close(); 
    }
}

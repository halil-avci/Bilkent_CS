package lab3;

/*
 * Lab03_Q2
 * 
 * This program takes a positive integer as input from the user,
 * displays its digit number, and verifies whether it is a palindromic number
 */

import java.util.Scanner;

public class Lab03_Q2 {
    public static void main(String[] args) {
        
        //Get input from the user
        Scanner in = new Scanner(System.in);
        System.out.print( "Enter a number: ");
        int input = in.nextInt();

        //Find digit number, initialize a boolean object
        int digitNumber = String.valueOf( input).length();
        Boolean isPalindromic = false;
        
        //Find whether input is in appropriate limits
        if (digitNumber < 3 || digitNumber > 7) {
            System.out.println( "The input is invalid! The number must" +
                " be between 3 and 7 digits long.");
            System.out.printf( "The number has %d digits.%n", digitNumber);
        }
        else {
            
            //Turn the input into a string
            System.out.printf( "The number has %d digits.%n", digitNumber);
            String str = String.valueOf( input);
            
            //According to digit number, test the inputs if they are palindrome or not
            if (digitNumber == 3) {
                if (str.substring( 0, 1).equals( str.substring( 2))) {
                    isPalindromic = true;
                }
            }
            else if (digitNumber == 4) {
                if (str.substring( 0, 1).equals( str.substring( 3))) {
                    if (str.substring( 1, 2).equals( str.substring( 2, 3))) {
                        isPalindromic = true;
                    }
                }
            }
            else if (digitNumber == 5) {
                if (str.substring( 0, 1).equals( str.substring( 4))) {
                    if (str.substring( 1, 2).equals( str.substring( 3, 4))) {
                        isPalindromic = true;
                    }
                }
            }
            else if (digitNumber == 6) {
                if (str.substring( 0, 1).equals( str.substring( 5))) {
                    if (str.substring( 1, 2).equals( str.substring( 4, 5))) {
                        if (str.substring( 2, 3).equals( str.substring( 3, 4))) {
                            isPalindromic = true;
                        }
                    }
                }
            }
            else {
                if (str.substring( 0, 1).equals( str.substring( 6))) {
                    if (str.substring( 1, 2).equals( str.substring( 5, 6))) {
                        if (str.substring( 2, 3).equals( str.substring( 4, 5))) {
                            isPalindromic = true;
                        }
                    }
                }
            }

            if (isPalindromic == true) {
                System.out.println( input + " is a palindromic number.");
            }
            else {
                System.out.println( input + " is NOT a palindromic number.");
            }
        }
        in.close();
    }
}
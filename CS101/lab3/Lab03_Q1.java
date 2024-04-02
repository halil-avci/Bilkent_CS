package lab3;

/**
 * Lab03_Q1
 * 
 * This program takes credit units and CGPA inputs from user, tells if the given inputs are satisfied or not.
 */

import java.util.Scanner;

public class Lab03_Q1 {
    public static void main(String[] args) {
        
        //Take input from user
        Scanner in = new Scanner( System.in);
        
        System.out.print( "Enter your credit units: ");
        int creditUnits = in.nextInt();

        System.out.print( "Enter your CGPA: ");
        double CGPA = in.nextDouble();

        //Compare the points 
        //Tell if graduation requirements are satisfied or not
        if (creditUnits > 120) {
            if (CGPA > 2.00) {
                System.out.println( "The graduation requirements are satisfied.");
            }
            else {
                System.out.println( "The CGPA is not sufficient.");
                System.out.println( "The graduation requirements are NOT satisfied.");
            }
        }
        else {
            System.out.println( "The credit units are not sufficient.");
            System.out.println( "The graduation requirements are NOT satisfied.");
        }
        in.close();
    }
}
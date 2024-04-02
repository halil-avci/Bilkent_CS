package lab2;

/**
 * Lab02_Q1
 * 
 * This program calculates the area and circumference of the ellipse with given sizes
 */

import java.util.Scanner;

public class Lab02_Q1 {

    public static void main( String[] args) {

        //Initialize number Pi
        double PI = 3.14159265359;
       
        //Get the ellipse's sizes from the user
        Scanner in = new Scanner( System.in);   
        System.out.print( "Enter length of the semi major axis of the ellipse: ");
        double semiMajorAxis = in.nextDouble();
        System.out.print( "Enter length of the semi minor axis: ");
        double semiMinorAxis = in.nextDouble();

        //Calculate area and circumference of ellipse
        double area = PI * semiMajorAxis * semiMinorAxis;
        double circumference = 2 * PI * Math.sqrt( ( semiMajorAxis * semiMajorAxis + semiMinorAxis * semiMinorAxis) / 2);

        //Print the values
        System.out.printf( "%nThe area of the ellipse is %14s %15.3f%n", ":", area);
        System.out.printf( "The circumference of the ellipse is ~ %3s %15.3f", ":", circumference);

        in.close();
    }
}
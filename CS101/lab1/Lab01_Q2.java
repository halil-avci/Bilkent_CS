/**
 * Lab01_Q2
 * 
 * This program calculates the result of some mathematical operations
 * and prints the results.
 * 
 */
public class Lab01_Q2 {

    public static void main(String[] args) {

        //Variables
        double result1;
        double result2;
        double result3;

        //Calculate and initialize the results of variables
        result1 = (32.2 - 17 / 22) / ((1.5 - 7.3) * (4.3 + 24));
        result2 = (73.5 * 16.4 - Math.pow( 3, 2) * 81) / (Math.pow( 2, 5) + 34);
        result3 = Math.pow( (2.4 - 0.4), -2.0/6);

        //Print the results
        System.out.println( "Result of expression 1 is: " + result1);
        System.out.println( "Result of expression 2 is: " + result2);
        System.out.println( "Result of expression 3 is: " + result3);
    }
}
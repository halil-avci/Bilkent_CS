package lab4;

/**
 * Lab04_Q4
 * 
 * This program calculates the area under the graph between x=0 and x=1
 * 
 */

public class Lab04_Q4 {
    public static void main(String[] args) {
        System.out.println( "The function is: sin(PI*x) + sin(PI*3*x)/3");
        
        //Initialize variables
        double x_start = 0;
        double x_end = 1;
        double step_size = 0.01;
        double total_area = 0;

        System.out.printf( "Parameters:%nx_start = 0, x_end = 1%nstep_size = 0.01%n");

        //Calculate the area under the graph
        while (x_start < x_end) {
            x_start = x_start + step_size;
            total_area = total_area + step_size * (Math.sin( Math.PI * x_start) + Math.sin( Math.PI * 3 * x_start) / 3);
        }

        //Print the result
        System.out.printf( "Area under \"sin(PI*x) + sin(PI*3*x)/3\" from 0 to 1: " + total_area);
    }
}
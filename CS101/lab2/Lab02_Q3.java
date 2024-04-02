package lab2;

import java.util.Scanner;

public class Lab02_Q3 {
    
    public static void main(String[] args) {

        //Get a string from the user
        Scanner in = new Scanner( System.in);
        System.out.print( "Enter the title: ");
        String title = in.nextLine();

        //Print asked information by using string methods
        System.out.println( "--------------------------------------");
        System.out.println( "Number of characters:" + title.length());
        System.out.printf( "All lowercase:\"%s\"%n", title.toLowerCase());
        System.out.printf( "Remove leading and trailing blank characters:\"%s\"%n", title.strip());
        System.out.printf( "Character at index position 4:'%s'%n", title.substring(4,5));
        System.out.printf( "Title from 3rd character to 5th character (both included):\"%s\"%n", title.substring(2,5));
        System.out.println( "First occurrence of character 'P':" + title.indexOf("P"));
        System.out.println( "Last occurrence of character 'P':" + title.lastIndexOf("P"));

        in.close();
    }
}

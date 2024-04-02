package lab3;

/*
 * Lab03_Q3
 * 
 * This is a PvP game program. In this game user can upgrade their armor, add a buddy or update their credentials. 
 */

import java.util.Scanner;

public class Lab03_Q3 {
    public static void main(String[] args) {
        Scanner in = new Scanner( System.in);

        System.out.print( "Enter your username: ");
        String username = in.next();
        
        //Username check
        if (username.equals("JavaWarrior")) {
            System.out.print( "Enter your password: ");
            String password = in.next();

            //Password check
            if (password.equals("JavaRocks")) {

                //Assign the info of the user
                int coins = 600;
                String buddyName = "none";

                //Bring the menu
                System.out.printf( "1- Upgrade armor%n2- Add a buddy%n3- Change credentials%n");
                System.out.print( "Select an operation: ");
                int operation = in.nextInt();

                //Upgrade Armor option
                if (operation == 1) {
                    System.out.println( "Upgrade armor:");
                    System.out.printf( "You have %d coins.%n", coins);

                    if (coins < 150) {
                        System.out.println( "Not enough coins! Bye!");
                    }
                    else {
                        coins = coins - 150;
                        System.out.println( "Your armor has been upgraded!");
                        System.out.printf( "You have %d coins. Bye!", coins);
                    }
                }
                //Add a buddy option
                else if (operation == 2) {
                    System.out.println( "Add a buddy:");

                    if (buddyName.equals( "none")) {
                        System.out.print( "Enter your buddy's name: ");
                        buddyName = in.next();
                        System.out.printf( "Your buddy is %s. Bye!", buddyName);
                    }
                    else {
                        System.out.println( "You already have a buddy!");
                        System.out.printf( "Your buddy is %s. Bye!", buddyName);
                    }
                }
                //Change credentials option
                else {
                    System.out.printf( "Change credentials:%n1- Change username%n2- Change password%n");
                    System.out.print( "Select an option: ");
                    int option = in.nextInt();

                    //Change username
                    if (option == 1) {
                        System.out.print( "Enter your new username: ");
                        username = in.next();
                    }
                    //Change password
                    else {
                        System.out.print( "Enter your new password: ");
                        String newPassword = in.next();

                        if (newPassword.length() > 20) {
                            System.out.print( "The password must have a maximum of 20 characters");
                        }
                        else {
                            password = newPassword;
                        }
                    }
                    System.out.printf( "Your username is %s%nYour password is %s%nBye!%n", username, password);
                }
            }
            else {
                System.out.println( "Wrong password! Bye!");
            }
        }
        else {
            System.out.println( "Username not found! Bye!");
        }
        in.close();
    }
}

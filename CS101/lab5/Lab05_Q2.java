package lab5;

import java.util.Random;

public class Lab05_Q2 {
    public static void main(String[] args) {
        //Create the deck string
        String deck = "";
        for (int i = 1; i <= 13; i++) {
            if (i < 10) {
                for (int count = 0; count < 4; count++) {
                    deck = deck + String.valueOf(i);
                }
            }
            else if (i == 10) {
                for (int count = 0; count < 4; count++) {
                    deck = deck + "T";
                }
            }
            else if (i == 11) {
                for (int count = 0; count < 4; count++) {
                    deck = deck + "J";
                }
            }
            else if (i == 12) {
                for (int count = 0; count < 4; count++) {
                    deck = deck + "Q";
                }
            }
            else {
                for (int count = 0; count < 3; count++) {
                    deck = deck + "K";
                }
            }
        }
        
        System.out.printf( "Starting the game with the following deck:%n%s%n", deck);
        System.out.println();

        //Initialize players' variables
        System.out.println( "Initial cards are dealing...");
        String player1 = "";
        String player2 = "";
        Random rand = new Random();
        
        //Deal the cards one by one randomly
        for (int i = 51; i > 0; i--) {
            if (i % 2 == 1) {    
                int randomChoice = rand.nextInt( i);
                String card = deck.substring( randomChoice, randomChoice + 1);
                player1 += card;
                deck = deck.replaceFirst( card, "");
            }
            else {
                int randomChoice = rand.nextInt( i);
                String card = deck.substring( randomChoice, randomChoice + 1);
                player2 += card;
                deck = deck.replaceFirst( card, "");
            }
        }

        System.out.printf( "Player-1 hand: %s%n", player1);
        System.out.printf( "Player-2 hand: %s%n", player2);
        System.out.println();

        //Remove the pairs from both players' hands
        for (int i = 0; i < 26; i++) {
            String ch = player1.substring( i, i + 1);
            for (int check = 0; check < 26; check++) {
                if (i != check && !ch.equals("0")) {
                    if (ch.equals(player1.substring( check, check + 1))) {
                        player1 = player1.replaceFirst( ch, "0");
                        player1 = player1.replaceFirst( ch, "0");
                        ch = "0";
                    }
                }
            }
        }
        for (int i = 0; i < 25; i++) {
            String ch = player2.substring( i, i + 1);
            for (int check = 0; check < 25; check++) {
                if (i != check && !ch.equals("0")) {
                    if (ch.equals(player2.substring( check, check + 1))) {
                        player2 = player2.replaceFirst( ch, "0");
                        player2 = player2.replaceFirst( ch, "0");
                        ch = "0";
                    }
                }
            }
        }
        player1 = player1.replace( "0", "");
        player2 = player2.replace( "0", "");

        System.out.println( "Pairs are removed: ");
        System.out.printf( "Player-1 hand: %s%nPlayer-2 hand: %s%n", player1, player2);
        System.out.println();

        //Make players draw cards fromeach other until one of them has no card
        boolean finished = false;
        int winner = 0;

        while (!finished) {
            System.out.println( "Start Drawing...");
            
            //Select a card randomly from player1
            int randomCard = rand.nextInt( player1.length());
            String chosenCard = player1.substring( randomCard, randomCard + 1);
            System.out.printf( "Player-2 is drawing the card: %s from Player-1...%n", chosenCard);
            //Delete the card from player1, add to player2
            player1 = player1.replace( chosenCard, "");
            player2 += chosenCard;
            System.out.printf( "\tPlayer-1 hand: %s%n\tPlayer-2 hand: %s%n", player1, player2);
            System.out.println();

            //Check if the chosen card creates pair. If it does, remove the pair
            if (!chosenCard.equals("K")) {
                player2 = player2.replace( chosenCard, "");
            }
            System.out.printf( "Pairs are removed:%nPlayer-1 hand: %s%nPlayer-2 hand: %s%n", player1, player2);
            System.out.println();

            //Check if player2 has won
            if (player2.equals("")) {
                winner = 2;
                finished = true;
            }
            else {
                System.out.println( "Start Drawing...");
            
                //Select a card randomly from player2
                randomCard = rand.nextInt( player2.length());
                chosenCard = player2.substring( randomCard, randomCard + 1);
                System.out.printf( "Player-1 is drawing the card: %s from Player-2...%n", chosenCard);
                //Delete the card from player2, add to player1
                player2 = player2.replace( chosenCard, "");
                player1 += chosenCard;
                System.out.printf( "\tPlayer-1 hand: %s%n\tPlayer-2 hand: %s%n", player1, player2);
                System.out.println();

                //Check if the chosen card creates pair. If it does, remove the pair
                if (!chosenCard.equals("K")) {
                    player1 = player1.replace( chosenCard, "");
                }
                System.out.printf( "Pairs are removed:%nPlayer-1 hand: %s%nPlayer-2 hand: %s%n", player1, player2);
                System.out.println();

                //Check if player1 has won
                if (player1.equals("")) {
                    winner = 1;
                    finished = true;
                }
            }

        }

        //Print winner
        System.out.println( "Game Over!");
        System.out.printf( "Player-%d Wins!%n", winner);
        System.out.printf( "\tPlayer-1 hand: %s%n\tPlayer-2 hand: %s%n", player1, player2);
        System.out.println();
    }   
}

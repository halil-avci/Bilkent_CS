package lab2;

import java.util.Scanner;

public class Lab02_Q2 {
    
    public static void main( String[] args) {

        double avTotalCost = 237760;
        double siteWork = 15903;
        double foundations = 25671;
        double framing = 41123;
        double exterior = 33066;
        double utility = 32746;
        double interiorFinishes = 67939;
        double outdoor = 16591;
        double unexpectedCosts = avTotalCost - ( siteWork + foundations + framing + exterior + utility + interiorFinishes + outdoor);

        double PSITEWORK = 100 * siteWork / avTotalCost;
        double PFOUNDATIONS = 100 * foundations / avTotalCost;
        double PFRAMING = 100 * framing / avTotalCost;
        double PEXTERIOR = 100 * exterior / avTotalCost;
        double PUTILITY = 100 * utility / avTotalCost;
        double PINTERIORFINISHES = 100 * interiorFinishes / avTotalCost;
        double POUTDOOR = 100 * outdoor / avTotalCost;
        double PUNEXPECTEDCOSTS = 100 * unexpectedCosts / avTotalCost;

        Scanner in = new Scanner( System.in);
        System.out.print( "Enter the cost of building a house in USD: ");
        double costInput = in.nextDouble();

        siteWork = costInput / 100 * PSITEWORK;
        foundations = costInput / 100 * PFOUNDATIONS;
        framing = costInput / 100 * PFRAMING;
        exterior = costInput / 100 * PEXTERIOR;
        utility = costInput / 100 * PUTILITY;
        interiorFinishes = costInput / 100 * PINTERIORFINISHES;
        outdoor = costInput / 100 * POUTDOOR;
        unexpectedCosts = costInput / 100 * PUNEXPECTEDCOSTS;

        System.out.printf( "%n*************************************************%n");
        System.out.printf( "*****%34s%10s", "House Cost Distribution Table", "*****");
        System.out.printf( "%n*************************************************%n");
        System.out.printf( "* Site Work%13s%d%19.2f%5s%n", "%", (int) PSITEWORK, siteWork, "*");
        System.out.printf( "* Foundations%11s%d%18.2f%5s%n", "%", (int) PFOUNDATIONS, foundations, "*");
        System.out.printf( "* Framing%15s%d%18.2f%5s%n", "%", (int) PFRAMING, framing, "*");
        System.out.printf( "* Exterior%14s%d%18.2f%5s%n", "%", (int) PEXTERIOR, exterior, "*");
        System.out.printf( "* Utility%15s%d%18.2f%5s%n", "%", (int) PUTILITY, utility, "*");
        System.out.printf( "* Interior Finishes%5s%d%18.2f%5s%n", "%", (int) PINTERIORFINISHES, interiorFinishes, "*");
        System.out.printf( "* Outdoor%15s%d%19.2f%5s%n", "%", (int) POUTDOOR, outdoor, "*");
        System.out.printf( "* Unexpected Costs%6s%d%19.2f%5s%n", "%", (int) PUNEXPECTEDCOSTS, unexpectedCosts, "*");
        System.out.printf( "* TOTAL%37.2f%5s", costInput, "*");
        System.out.printf( "%n*************************************************");

        in.close();
    }
}

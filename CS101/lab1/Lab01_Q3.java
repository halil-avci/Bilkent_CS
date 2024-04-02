/**
 * Lab01_Q3
 * 
 * This program calculates and answers some questions about mass and number of atoms of elements for a human body. 
 */
public class Lab01_Q3 {

    public static void main(String[] args) {
        
        //Initialize given constants
        final double OXYGEN_MASS_PERCENTAGE = 65;
        final double CARBON_MASS_PERCENTAGE = 18.5;
        final double HYDROGEN_MASS_PERCENTAGE = 10;
        final double NITROGEN_MASS_PERCENTAGE = 3.2;
        final double CALCIUM_MASS_PERCENTAGE = 1.5;
        final double TOTAL_MASS_PERCENTAGE = 98.6;

        final double OXYGEN_ATOM_PERCENTAGE = 24;
        final double HYDROGEN_ATOM_PERCENTAGE = 62;

        final double TOTAL_ATOM_NUMBER = 7 * Math.pow( 10, 27);

        final double HUMAN_MASS = 70;

        //Find the mass percentage of phosphorus
        final double PHOSPHORUS_MASS_PERCENTAGE = TOTAL_MASS_PERCENTAGE - (OXYGEN_MASS_PERCENTAGE + CARBON_MASS_PERCENTAGE + HYDROGEN_MASS_PERCENTAGE + NITROGEN_MASS_PERCENTAGE + CALCIUM_MASS_PERCENTAGE);

        //Find the mass percentages of elements other than the ones specified
        final double OTHERS_MASS_PERCENTAGE = 100 - TOTAL_MASS_PERCENTAGE;

        //Find the number of atoms of elements other than the ones specified
        final double OTHERS_ATOM_PERCENTAGE = 100 - (OXYGEN_ATOM_PERCENTAGE + HYDROGEN_ATOM_PERCENTAGE);
        final double OTHERS_ATOM_NUMBER = TOTAL_ATOM_NUMBER * OTHERS_ATOM_PERCENTAGE / 100;

        //Calculate the mass of elements with the highest two ratios
        double massOfOxygen = HUMAN_MASS * OXYGEN_MASS_PERCENTAGE / 100;
        double massOfCarbon = HUMAN_MASS * CARBON_MASS_PERCENTAGE / 100;

        //Calculate the number of atoms of some elements
        double atomsOfOxygen = TOTAL_ATOM_NUMBER * OXYGEN_ATOM_PERCENTAGE / 100;
        double atomsOfHydrogen = TOTAL_ATOM_NUMBER * HYDROGEN_ATOM_PERCENTAGE / 100;

        //Print the answers of given questions
        System.out.println( "Phosphorus makes up " + PHOSPHORUS_MASS_PERCENTAGE + " percent of the mass in the human body.");
        
        System.out.println( "Elements other than oxygen, carbon, hydrogen, nitrogen, calcium and phosphorus make up " + OTHERS_MASS_PERCENTAGE + " percent of the mass with an atom count of " + OTHERS_ATOM_NUMBER);
        System.out.println();

        System.out.println( "For a person of " + HUMAN_MASS + " kg the mass of the elements are:");
        System.out.println( "Oxygen: " + massOfOxygen + "kg");
        System.out.println( "Carbon: " + massOfCarbon + "kg");
        System.out.println();

        System.out.println( "whereas the number of atoms of some elements in this person are:");
        System.out.println( "Hydrogen: " + atomsOfHydrogen);
        System.out.println( "Oxygen: " + atomsOfOxygen);
    }
}
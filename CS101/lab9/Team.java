package lab9;

import java.util.ArrayList;

public class Team {
    
    //Instance variables
    private int ID;
    private String name;
    private int averageAge;
    private int marketValue;
    private ArrayList<Player> squad;

    //Constructor
    public Team( int ID, String name) {
        if (ID > 0) {
            this.ID = ID;
        }
        this.name = name;
        this.averageAge = 0;
        this.marketValue = 0;
        this.squad = new ArrayList<>();
    }

    //Accessors
    public int getID() {
        return this.ID;
    }
    public String getName() {
        return this.name;
    }
    public int getAverageAge() {
        return this.averageAge;
    }
    public int getMarketValue() {
        return this.marketValue;
    }
    public ArrayList<Player> getSquad() {
        return this.squad;
    }

    //Methods

    /**
     * Returns true if a player with a specific jersey number exists in the team
     * @param jerseyNumber
     * @return
     */
    public boolean playerExists( int jerseyNumber) {
        for (Player player : squad) {
            if (player.getJerseyNumber() == jerseyNumber) {
                return true;
            }
        }
        return false;
    }

    /**
     * takes a Player object as parameter and adds this player to the team if the 
     * player does not exist in the team and the player is a citizen of that country
     * @param player
     */
    public void addPlayer( Player player) {
        boolean present = false;
        for (Player person : squad) {
            if (person == player)
            present = true;
        }

        if (!present && player.getNationality().equals( this.name)) {
            squad.add( player);

            int totalAge = 0;
            int counter = 0;
            for (int c = 0; c < squad.size(); c++) {
                totalAge += squad.get( c).getAge();
                counter++;
            }
            this.averageAge = totalAge / counter;
            this.marketValue += player.getMarketValue(); 
        } 
    }

    /**
     * removes the player from the team with the specific jersey number
     * @param jerseyNumber
     */
    public void removePlayer( int jerseyNumber) {
        for (int i = 0; i < squad.size(); i++) {
            Player player = squad.get( i);
            if (player.getJerseyNumber() == jerseyNumber) {
                squad.remove( i);

                int totalAge = 0;
                int counter = 0;
                for (int c = 0; c < squad.size(); c++) {
                    totalAge += squad.get( c).getAge();
                    counter++;
                }
                this.averageAge = totalAge / counter;
                this.marketValue -= player.getMarketValue();
            }
        }
    }

    //Override toString method
    public String toString() {
        String valueString = String.valueOf( this.marketValue);
        String valueResult = "";
        while (valueString.length() > 3) {
            String triple = valueString.substring( valueString.length() - 3, valueString.length());
            valueResult = "," + triple + valueResult;
            valueString = valueString.substring( 0, valueString.length() - 3);
        }
        valueResult = valueString + valueResult;

        String seperator = "=================================================================================\n";
        String header = "=" + "\t\t\t\t  Team Details  \t\t\t\t" + "=\n";   
        String features = "ID: " + this.ID + "\nTeam: " + this.name + "\nAverage Age: " +
            this.averageAge + "\nMarket Value: " + valueResult;
        String subHeader = "\nSquad is composed of following players:\n";
        String subSeperator = "---------------------------------------------------------------------------------\n";
        String categories = "Name\t\t    Age\tNationality\tNumber\tPosition\t    Market Value\n";
        
        String players = "";
        for (Player person : squad) {
            players = players + person + "\n";
        }

        return seperator + header + seperator + features + subHeader + subSeperator + categories +
            subSeperator + players + seperator;
    }
}
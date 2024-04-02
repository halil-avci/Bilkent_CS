package lab9;

import java.util.Arrays;

public class Group {
    
    //Instance variables
    private String name;
    private int groupSize;
    private int numberOfTeams;
    private Team[] teams;
    private Game[][] games;
    private int[] points;

    //Constructor
    public Group( String name, int groupSize) {
        this.name = name;
        if (groupSize > 0) {
            this.groupSize = groupSize;
        }
        this.numberOfTeams = 0;
        this.teams = new Team[groupSize];
        this.games = new Game[groupSize][groupSize - 1];
        this.points = new int[groupSize];
    }

    //Accessors
    public String getName() {
        return this.name;
    }
    public int getGroupSize() {
        return this.groupSize;
    }
    public int getNumberOfTeams() {
        return this.numberOfTeams;
    }
    public Team[] getTeams() {
        return this.teams;
    }

    //Group methods

    /*
     * Returns true if the team with the given ID exists in the group
     */
    public boolean teamExists( int teamID) {
        for (int i = 0; i < numberOfTeams; i++) {
            if (this.teams[i].getID() == teamID) {
                return true;
            }
        }
        return false;
    }

    /*
     * Adds a team to the group if the team does not already exist in the 
     * group and there is room in the group
     */
    public void addTeam( Team team) {
        if (teamExists( team.getID())) {
            System.out.println( "Team already exists in the group!");
        }
        else if (this.numberOfTeams >= this.groupSize) {
            System.out.println( "Group already has " + numberOfTeams + "/" + groupSize + " teams.");
        }
        else {
            teams[this.numberOfTeams] = team;
            this.numberOfTeams++;
        }
    }

    /*
     * Adds a game to the group by updating the individual team game properties in the group captured by 
     * the games data member. The game is added only if both teams of the game belong to the same group. 
     * Furthermore, we assume that there is only one game between the teams (there is no concept of 
     * Home vs. Visitor in the world cup). Additional games added between the same teams will be ignored. 
     * When the game is added, points for the teams are updated accordingly.
     */
    public void addGame( Game game) {
        boolean alreadyExists = false;
        for (Team element1 : teams) {
            if (game.getTeams()[0] == element1) {

                for (Team element2 : teams) {
                    if (game.getTeams()[1] == element2) {

                        for (int t = 0; t < game.getTeams().length; t++) {

                            for (int i = 0; i < this.groupSize; i++) { 
                                if (game.getTeams()[t] == teams[i]) {
                                    boolean done = false;
                                    for (int j = 0; j < groupSize - 1; j++) {
                                        if (games[i][j] != null) {
                                            if (games[i][j].getTeams()[0] == game.getTeams()[0] || games[i][j].getTeams()[0] == game.getTeams()[1]) {
                                                if (games[i][j].getTeams()[1] == game.getTeams()[0] || games[i][j].getTeams()[1] == game.getTeams()[1]) {
                                                    alreadyExists = true;
                                                    done = true;
                                                }
                                            }
                                        }
                                            
                                        if (games[i][j] == null && !done) {
                                            games[i][j] = game;
                                            this.points[i] += game.getTeamPoints( teams[i].getID());
                                            done = true;
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        if (alreadyExists) {
            System.out.println( "Already a game between the teams exists!");
        }
    }

    //Override toString method
    public String toString() {
        String seperator = "==================================\n";
        String header = "=  \tGroup " + this.name + " Standings\t =\n";
        
        String fixture = "";
        int[] copyPoints = Arrays.copyOf( this.points, this.points.length);
        for (int i = 0; i < numberOfTeams; i++) {
            
            int highest = copyPoints[0];
            int indexOfHighest = 0;
            for (int c = 1; c < copyPoints.length; c++) {
                if (copyPoints[c] > highest) {
                    highest = copyPoints[c];
                    indexOfHighest = c;
                }
            }

            String fixtureLine = String.format("  %d.%13s ( %2d )   %d      \n", (i + 1),
                this.teams[indexOfHighest].getName(), this.teams[indexOfHighest].getID(), copyPoints[indexOfHighest]);
            
            fixture += fixtureLine;

            copyPoints[indexOfHighest] = -1;
        }

        return seperator + header + seperator + fixture + seperator;
    }
}

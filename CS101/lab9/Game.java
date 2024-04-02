package lab9;

public class Game {
    
    //Instance variables
    private Team[] teams;
    private int[] goals;

    //Constructor
    public Game( Team team1, Team team2, int team1Goals, int team2Goals) {
        this.teams = new Team[2];
        this.teams[0] = team1;
        this.teams[1] = team2;

        if (team1Goals >= 0 && team2Goals >= 0) {
            this.goals = new int[2];
            this.goals[0] = team1Goals;
            this.goals[1] = team2Goals;
        }
    }

    //Accessor
    public Team[] getTeams() {
        return this.teams;
    }

    //Game Methods

    /*
     * Returns the points obtained from this game for a 
     * given team with its team ID.
     */
    public int getTeamPoints( int teamID) {
        final int WINNER = 3;
        final int DRAW = 1;
        final int LOSER = 0;

        if (teams[0].getID() == teamID) {
            
            if (goals[0] > goals[1]) {
                return WINNER;
            }
            else if (goals[0] == goals[1]) {
                return DRAW;
            }
            else {
                return LOSER;
            }
        }
        else {

            if (goals[0] > goals[1]) {
                return LOSER;
            }
            else if (goals[0] == goals[1]) {
                return DRAW;
            }
            else {
                return WINNER;
            }
        }
    }

    //Override toString method
    public String toString() {
        String team1 = teams[0].getName();
        String team2 = teams[1].getName();
        int score1 = goals[0];
        int score2 = goals[1];

        return team1 + " vs. " + team2 + ": " + score1 + "-" + score2 + "\n";
    }
}

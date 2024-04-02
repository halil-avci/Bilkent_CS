package lab9;
/** A class for Qatar 2022 World Cup
*   Turkiye is also qualified in this version :)
*   Market values and player information is obtained from Transfermarkt.com
*   @author Ozcan Ozturk
*   @version 1.0
*/
import java.util.Scanner;

public class Qatar2022 {
    /**
     * @param args
     */
    public static void main(String[] args) {        
        // Form the English Team
        Team england = new Team(34, "England");
        england.addPlayer(new Player("Raheem Sterling",  27, "England", 17, "Left Wing", 70000000));
        england.addPlayer(new Player("Phil Foden",  22, "England", 47, "Central Midfield", 110000000));
        england.addPlayer(new Player("Jack Grealish",  27, "England", 10, "Left Wing", 70000000));
        england.addPlayer(new Player("Declan Rice",  23, "England", 41, "Defensive Midfield", 80000000));
        england.addPlayer(new Player("Declan Rice",  23, "England", 41, "Defensive Midfield", 80000000));
        england.addPlayer(new Player("Aaron Ramsdale", 24, "England", 23, "Goalkeeper", 30000000)); 
        england.addPlayer(new Player("Aaron Ramsdale", 24, "England", 23, "Goalkeeper", 30000000));
        england.addPlayer(new Player("Jordan Pickford", 28, "England", 1, "Goalkeeper", 28000000));
        england.addPlayer(new Player("Nick Pope", 30, "England", 13, "Goalkeeper", 18000000));
        england.addPlayer(new Player("Ben White", 25, "England", 21, "Centre Back", 45000000)); 
        england.addPlayer(new Player("John Stones", 28, "England", 5, "Centre Back", 30000000));	
        england.addPlayer(new Player("Harry Maguire", 29, "England", 6, "Centre Back", 30000000));
        england.addPlayer(new Player("Eric Dier", 28, "England", 15, "Centre Back", 30000000));
        england.addPlayer(new Player("Conor Coady", 29, "England", 16, "Centre Back", 18000000));
        england.addPlayer(new Player("Luke Shaw", 27, "England", 3, "Left Back", 28000000)); 
        england.addPlayer(new Player("Kyle Walker", 32, "England", 2, "Right Back", 15000000)); 
        england.addPlayer(new Player("Jude Bellingham", 19, "England", 22, "Central Midfield", 100000000));
        england.addPlayer(new Player("Harry Kane", 29, "England", 9, "Centre Forward", 90000000));

        // Form the Turkish Team
        Team turkiye = new Team(38, "Türkiye");
        turkiye.addPlayer(new Player("Ugurcan Çakir", 26, "Türkiye", 23, "Goalkeeper", 14000000));
        turkiye.addPlayer(new Player("Altay Bayindir", 24, "Türkiye", 1, "Goalkeeper", 13000000)); 
        turkiye.addPlayer(new Player("Çaglar Söyüncü",	26, "Türkiye", 4, "Centre Back", 22000000)); 
        turkiye.addPlayer(new Player("Ozan Kabak", 22, "Türkiye", 15, "Centre Back", 10000000)); 
        turkiye.addPlayer(new Player("Tayyip Sanuç", 22, "Türkiye", 6, "Centre Back", 3800000)); 
        turkiye.addPlayer(new Player("Eren Elmali", 22, "Türkiye", 13, "Left Back", 4200000)); 
        turkiye.addPlayer(new Player("Zeki Çelik", 25, "Türkiye", 2, "Right Back", 15000000)); 
        turkiye.addPlayer(new Player("Salih Özcan", 24, "Türkiye", 5, "Defensive Midfield", 17000000));
        turkiye.addPlayer(new Player("Hakan Çalhanoglu", 28, "Türkiye", 10, "Central Midfield", 35000000));
        turkiye.addPlayer(new Player("Arda Güler", 17, "Türkiye", 25, "Attacking Midfield", 10000000));
        turkiye.addPlayer(new Player("Kerem Aktürkoglu", 24, "Türkiye", 7, "Left Wing", 13000000));
        turkiye.addPlayer(new Player("Cengiz Ünder", 25, "Türkiye", 17, "Right Wing", 17000000));
        turkiye.addPlayer(new Player("Enes Ünal", 25, "Türkiye", 16, "Centre Forward", 25000000));
        turkiye.addPlayer(new Player("Umut Bozok", 26, "Türkiye", 19, "Centre Forward", 5500000));
        turkiye.addPlayer(new Player("Cenk Tosun", 31, "Türkiye", 9, "Centre Forward", 2000000));

        // Form the Germany Team
        Team germany = new Team(6, "Germany");
        germany.addPlayer(new Player("Andre Ter Stegen", 30, "Germany", 22, "Goalkeeper", 30000000)); 
        germany.addPlayer(new Player("Manuel Neuer", 36, "Germany", 1, "Goalkeeper", 12000000));
        germany.addPlayer(new Player("Antonio Rüdiger", 29, "Germany", 2, "Centre Back", 40000000)); 
        germany.addPlayer(new Player("Niklas Süle", 27, "Germany", 15, "Centre Back", 35000000));
        germany.addPlayer(new Player("Thilo Kehrer", 26, "Germany", 5, "Centre Back", 22000000)); 
        germany.addPlayer(new Player("David Raum", 24, "Germany", 3, "Left Back", 26000000)); 
        germany.addPlayer(new Player("Lukas Klostermann", 26, "Germany", 16, "Right Back", 14000000)); 
        germany.addPlayer(new Player("Joshua Kimmich", 27, "Germany", 6, "Defensive Midfield", 80000000));
        germany.addPlayer(new Player("Leon Goretzka", 27, "Germany", 8, "Central Midfield", 65000000));
        germany.addPlayer(new Player("Ilkay Gündogan", 32, "Germany", 21, "Central Midfield", 25000000));
        germany.addPlayer(new Player("Jamal Musiala", 19, "Germany", 14, "Attacking Midfield", 100000000));
        germany.addPlayer(new Player("Leroy Sane", 26, "Germany", 19, "Left Wing", 70000000));
        germany.addPlayer(new Player("Serge Gnabry", 27, "Germany", 10, "Right Wing", 65000000));
        germany.addPlayer(new Player("Karim Adeyemi", 20, "Germany", 24, "Right Wing", 35000000));
        germany.addPlayer(new Player("Youssoufa Moukoko", 18, "Germany", 26, "Centre Forward", 30000000));
        germany.addPlayer(new Player("Niclas Füllkrug", 29, "Germany", 9, "Centre Forward", 5000000));
        
        // Create a Group to play the matches in the group
        // Group is created with 4 teams but 3 teams have already
        // been created manually to have some data ready to be used.
        Group groupA = new Group("A", 4);

        // Add the teams to Group "A"
        groupA.addTeam(germany);
        groupA.addTeam(england);
        groupA.addTeam(turkiye);

        //Print the menu
        String seperator = "---------------------------------------------------\n";
        System.out.print( seperator + "Welcome to Qatar 2022! Get ready for the World Cup!\n" + seperator);

        boolean finished = false;
        while (!finished) {
            System.out.print( "-------------- Group: " + groupA.getName() + " -------------------\n");
            System.out.print( "1 - Create a new Team\n2 - Display a Team\n3 - Add a player to a Team\n" +
                "4 - Remove a Player with ID from a team\n5 - Add a game to the group\n6 - Display Standings\n7 - Exit\n" + seperator + "Your choice: ");

            Scanner in = new Scanner( System.in);
            int choice = in.nextInt();

            //Choices
            if (choice == 1) {

                if (groupA.getNumberOfTeams() < groupA.getGroupSize()) {
                    System.out.print( "What is the uniqe ID of the Team?: ");
                    int teamID = in.nextInt();
                    if (teamID > 0) {
                        System.out.print( "What is the name of the Team?: ");
                        String teamName = in.next();

                        Team newTeam = new Team( teamID, teamName);
                        groupA.addTeam( newTeam);
                    }
                    else {
                        System.out.println( "Team ID cannot be negative!");
                    }
                }
                else {
                    System.out.println( "Group already has " + groupA.getNumberOfTeams() + "/" + groupA.getGroupSize() + " teams.");
                }
            }

            else if (choice == 2) {
                System.out.print( "What is the uniqe ID of the Team?: ");
                int teamID = in.nextInt();
                if (teamID > 0) {
                    if (groupA.teamExists( teamID)) {
                        for (int i = 0; i < groupA.getTeams().length; i++) {
                            if (groupA.getTeams()[i] != null) {
                                if (groupA.getTeams()[i].getID() == teamID) {
                                    System.out.print( groupA.getTeams()[i]);
                                }
                            }
                        }
                    }
                    else {
                        System.out.println( "Team does not exist!");
                    }
                }
                else {
                    System.out.println( "Team ID cannot be negative!");
                }
            }
            
            else if (choice == 3) {
                System.out.print( "What is the uniqe ID of the Team to add the Player?: ");
                int teamID = in.nextInt();
                if (teamID > 0) {
                    if (groupA.teamExists( teamID)) {
                        
                        System.out.print( "Enter the name of the player: ");
                        in.nextLine();
                        String name = in.nextLine();

                        System.out.print( "Enter the age of the player: ");
                        int age = in.nextInt();

                        System.out.print( "Enter the nationality of the player: ");
                        in.nextLine();
                        String nationality = in.nextLine();
                        String teamNationality = "";
                        Team team = null;
                        for (int i = 0; i < groupA.getTeams().length; i++) {
                            if (groupA.getTeams()[i] != null) {   
                                if (groupA.getTeams()[i].getID() == teamID) {
                                    team = groupA.getTeams()[i];
                                    teamNationality = team.getName();
                                }
                            }
                        }
                        if (teamNationality.equals( nationality)) {

                            System.out.print( "Enter the jersey number of the player: ");
                            int jerseyNumber = in.nextInt();
                            boolean jerseyNumberExists = false;
                            for (int c = 0; c < team.getSquad().size(); c++) {
                                if (team.getSquad().get(c).getJerseyNumber() == jerseyNumber) {
                                    jerseyNumberExists = true;
                                }
                            }

                            if (!jerseyNumberExists) {
                                
                                System.out.print( "Enter the position of the player: ");
                                in.nextLine();
                                String position = in.nextLine();

                                System.out.print( "Enter the market value of the player: ");
                                int marketValue = in.nextInt();
                                if (marketValue > 0) {

                                    Player newPlayer = new Player(name, age, nationality, jerseyNumber, position, marketValue);
                                    team.addPlayer( newPlayer);
                                }
                                else {
                                    System.out.println( "Market value cannot be negative!");
                                }
                            }
                            else {
                                System.out.println( "Player with jersey number already exists!");
                            }
                        }
                        else {
                            System.out.println( "Player must be a citizen of the country!");
                        }
                    }
                    else {
                        System.out.println( "Team does not exist!");
                    }
                }
                else {
                    System.out.println( "Team ID cannot be negative!");
                }
            }

            else if (choice == 4) {
                System.out.print( "What is the uniqe ID of the Team to remove the Player?: ");
                int teamID = in.nextInt();
                if (teamID > 0) {
                    if (groupA.teamExists( teamID)) {
                        
                        Team team = null;
                        for (int i = 0; i < groupA.getTeams().length; i++) {
                            if (groupA.getTeams()[i] != null) {   
                                if (groupA.getTeams()[i].getID() == teamID) {
                                    team = groupA.getTeams()[i];
                                }
                            }
                        }

                        System.out.print( "Enter the jersey number of the player: ");
                        int jerseyNumber = in.nextInt();
                        boolean jerseyNumberExists = false;
                        for (int c = 0; c < team.getSquad().size(); c++) {
                            if (team.getSquad().get(c).getJerseyNumber() == jerseyNumber) {
                                jerseyNumberExists = true;
                            }
                        }

                        if (jerseyNumberExists) {

                            team.removePlayer(jerseyNumber);
                        }
                        else {
                            System.out.println( "Player does not exist!");
                        }
                    }
                    else {
                        System.out.println( "Team does not exist!");
                    }
                }
                else {
                    System.out.println( "Team ID cannot be negative!");
                }
            }
            else if (choice == 5) {
                System.out.print( "What is the uniqe ID for the First Team?: ");
                int teamID1 = in.nextInt();
                if (teamID1 > 0) {
                    if (groupA.teamExists(teamID1)) {
                        
                        System.out.print( "What is the uniqe ID for the Second Team?: ");
                        int teamID2 = in.nextInt();

                        if (teamID2 > 0) {
                            if (groupA.teamExists(teamID2)) {

                                System.out.print( "Enter the score (such as 2 1): ");
                                String first = in.next();
                                String second = in.next();
                                int score1 = Integer.parseInt( first);
                                int score2 = Integer.parseInt(second);

                                if (score1 >= 0 && score2 >= 0) {

                                    Team team1 = null;
                                    for (int i = 0; i < groupA.getTeams().length; i++) {
                                        if (groupA.getTeams()[i] != null) {   
                                            if (groupA.getTeams()[i].getID() == teamID1) {
                                                team1 = groupA.getTeams()[i];
                                            }
                                        }
                                    }

                                    Team team2 = null;
                                    for (int i = 0; i < groupA.getTeams().length; i++) {
                                        if (groupA.getTeams()[i] != null) {   
                                            if (groupA.getTeams()[i].getID() == teamID2) {
                                                team2 = groupA.getTeams()[i];
                                            }
                                        }
                                    }

                                    Game newGame = new Game( team1, team2, score1, score2);
                                    groupA.addGame(newGame);
                                }
                                else {
                                    System.out.println( "Scores cannot be negative!");
                                }
                            }
                            else {
                                System.out.println( "Second team does not exist!");
                            }
                        }
                        else {
                            System.out.println( "Team ID cannot be negative!");
                        }
                    }
                    else {
                        System.out.println( "First team does not exist!");
                    }
                }
                else {
                    System.out.println( "Team ID cannot be negative!");
                }
                
            }

            else if (choice == 6) {
                System.out.println( groupA);
            }
            else {
                finished = true;
                in.close();
            }
        }
    }
}
package lab9;

public class Player {

    //Instance variables
    private String name;
    private int age;
    private String nationality;
    private int jerseyNumber;
    private String position;
    private int marketValue;

    //Constructor
    public Player( String name, int age, String nationality, int jerseyNumber, String position, int marketValue) {
        this.name = name;
        setAge( age);
        this.nationality = nationality;
        setJerseyNumber( jerseyNumber);
        this.position = position;
        setMarketValue( marketValue);
    }

    //Accessors
    public String getName() {
        return this.name;
    }
    public int getAge() {
        return this.age;
    }
    public String getNationality() {
        return this.nationality;
    }
    public int getJerseyNumber() {
        return this.jerseyNumber;
    }
    public String getPosition() {
        return this.position;
    }
    public int getMarketValue() {
        return this.marketValue;
    }

    //Setters
    public void setAge( int age) {
        if (age > 0) {
            this.age = age;
        }    
    }
    public void setJerseyNumber( int jerseyNumber) {
        if (jerseyNumber >= 1 && jerseyNumber <= 99) {
            this.jerseyNumber = jerseyNumber;
        }
    }
    public void setPosition( String position) {
        this.position = position;
    }
    public void setMarketValue( int marketValue) {
        if (marketValue > 0) {
            this.marketValue = marketValue;
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

        String stringName = this.name;
        for (int i = 0; i < 20 - this.name.length(); i++) {
            stringName += " ";
        }
        String stringPosition = this.position;
        for (int i = 0; i < 20 - this.position.length(); i++) {
            stringPosition += " ";
        }

        return stringName + this.age + "\t" + this.nationality + "\t\t" +
            this.jerseyNumber + "\t" + stringPosition + valueResult;
    }
    
}

package lab7;

/**
 * This program creates track objects
 */
public class Track {
    public static int count;
    public static int allCount;

    private int ID;
    private String title;
    private int album;
    private int artist;
    private String releaseDate;
    private int duration;
    private String genre;
    private boolean isActive;
    private long playCount;

    /**
     * Constructor
     */
    public Track( String title, int album, int artist, String releaseDate, int duration) {
        this.title = title;
        this.album = album;
        this.artist = artist;
        this.releaseDate = releaseDate;
        this.duration = duration;
        genre = "UN";
        isActive = true;

        count++;
        allCount++;
        ID = allCount;
    }

    /**
     * Accessors
     */
    public int getID() {
        return ID;
    }
    public String getTitle() {
        return title;
    }
    public int getAlbum() {
        return album;
    }
    public int getArtist() {
        return artist;
    }
    public String getReleaseDate() {
        return releaseDate;
    }
    public int getDuration() {
        return duration;
    }
    public String getGenre() {
        return genre;
    }
    public boolean getIsActive() {
        return isActive;
    }

    /**
     * Setters
     */
    public void setGenre( String input) {
        if (input.equals("PO") || input.equals("RO") || input.equals("JA") || input.equals("OT")) {
            genre = input;
        }
    }
    public void register() {
        allCount++;
        count++;
    }
    public void unregister() {
        isActive = false;
        count--;
    }

    /**
     * Compares dates of tracks
     * @param anotherTrack
     * @return
     */
    public boolean isBefore( Track anotherTrack) {
        String firstDate = this.releaseDate.substring( 6) + "/" + this.releaseDate.substring( 3, 5) + 
            "/" + this.releaseDate.substring( 0, 2);
        String secondDate = anotherTrack.getReleaseDate().substring( 6) + "/" + anotherTrack.getReleaseDate().substring( 3, 5) + 
            "/" + anotherTrack.getReleaseDate().substring( 0, 2);

        if (firstDate.compareTo( secondDate) < 0) {
            return true;
        }
        return false;
    }

    /**
     * Increases play count by 1 
     * Gives an error if track is inactive  
     */
    public void play() {
        if (isActive) {
            playCount++;
        }
        else {
            System.out.println( "play() called on inactive track!");
        }
    }

    /**
     * Increases play count as input
     * @param countToIncrement
     */
    public void playBatch( int countToIncrement) {
        playCount += countToIncrement;
    }

    /**
     * Override toString method
     */
    public String toString() {
        String stars = "*************************************\n";
        String header = "";
        if (isActive) {
            header = "Active track " + ID + " among " + count + " active tracks\n";
        }
        else {
            header = "Inactive track " + ID + " among " + allCount + " tracks\n";
        }
        
        String genreType = "Unspecified";
        if (genre.equals( "PO")) {
            genreType = "Popular";
        }
        else if (genre.equals( "RO")) {
            genreType = "Rock";
        }
        else if (genre.equals( "JA")) {
            genreType = "Jazz";
        }
        else if (genre.equals( "OT")) {
            genreType = "Other";
        }

        String features = "Title:\t" + title + "\nAlbum:\t" + album + "\nArtist:\t" + artist + "\nRelease:\t" + releaseDate +
            "\nLength:\t" + "?" + "\nGenre\t" + genreType + "\nPlayed:\t" + playCount + "\n";

        return stars + header + features + stars + "\n";
    }

    public static void main(String[] args) {
        Track t1 = new Track("Love over gold", 123, 234, "12/08/1982", (short)2473);
        t1.setGenre("RO");
        Track t2 = new Track("Gozleri aska gulen", 0, 98, "18/04/2018", (short)257);
        t2.setGenre("PO");
        Track t3 = new Track("Down to the waterline", 123, 234, "09/06/1978", (short)235);
        System.out.println("Is t1 before t2? " + t1.isBefore(t2));
        System.out.println("Is t2 before t3? " + t2.isBefore(t3));
        System.out.println();

        t1.play();
        t3.play();
        t3.play();
        t1.playBatch(100);
        t3.playBatch(10);
        t1.play();
        t2.playBatch(50);
        t1.unregister();
        t1.play();
        System.out.println(t1.toString());
        System.out.println(t2.toString());
        System.out.println(t3.toString());
    }
}   

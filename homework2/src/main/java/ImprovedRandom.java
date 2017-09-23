import java.util.Random;

public class ImprovedRandom extends Random{

    public ImprovedRandom(){
        super();
    }
    public ImprovedRandom(long seed){
        super(seed);
    }

    public int rangedNext(int lowerBound, int upperBound){
        return (this.nextInt((upperBound-lowerBound)) + lowerBound);
    }
}

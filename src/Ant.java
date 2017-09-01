public class Ant extends Creature{

    public Ant(String name){
        super(name );
    }

    public void move(){
        System.out.println(this.toString() + " " + this.getClass().getSimpleName() + " is crawling around.");
    }
}

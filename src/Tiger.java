public class Tiger extends Creature{

    public Tiger(String name){
        super(name);
    }

    public void move(){
        System.out.println(this.toString() + this.getClass().toString().substring(5) + " has just pounced.\n");
    }

}

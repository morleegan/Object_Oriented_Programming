public class Tiger extends Creature{

    public Tiger(String name){
        super(name);
    }

    public void move(){
        System.out.println(this.toString() +" "+ this.getClass().getSimpleName() + " has just pounced.\n");
    }

}

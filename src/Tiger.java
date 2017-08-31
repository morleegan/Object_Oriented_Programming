public class Tiger extends Creature{

    public Tiger(String name){
        super(name);
    }

    public void move(){
        System.out.println(this.toString() + this.getClassSubstring() + " has just pounced.\n");
    }

}

public class Bat extends Creature implements Flyer {

    public Bat(String name){
        super(name);
    }

    public void move(){
        this.fly();
    }

    public void fly(){
        System.out.println(this.toString() + this.getClassSubstring() + " is swooping through the dark.");
    }

}

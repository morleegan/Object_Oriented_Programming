public class Fly extends Creature implements Flyer{

    public Fly(String name){super(name); }

    @Override
    public void eat(Thing aThing) {
        if (!aThing.getClass().getSimpleName().equals("Thing")) {
            System.out.println(this.toString() + " " + this.getClass().getSimpleName() +
                    " won't eat a " + aThing.getClass().getSimpleName());
        }
        else {
            super.eat(aThing);
        }
    }

    public void move(){
        this.fly();
    }

    public void fly(){
        System.out.println(this.toString() + " " + this.getClass().getSimpleName() + " is buzzing around in flight.");
    }
}

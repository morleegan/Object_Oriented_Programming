public abstract class Creature extends Thing {
    private Thing inStomach;

    public Creature(String name){
        super(name);
    }

    public Thing getInStomach(){
        return this.inStomach;
    }

    public void eat(Thing aThing){
        this.inStomach = aThing;
        System.out.println(this.toString()
                + this.getClassSubstring() + " has just eaten a "+ aThing.toString());
    }

    public void whatDidYouEat(){
        if (this.inStomach != null){
            System.out.println(this.toString() + this.getClass().toString().substring(5)
                    + " has eaten a " + this.inStomach.toString() + this.getClassSubstring() + "!");
        }
        else {
            System.out.println(this.toString() + this.getClassSubstring() + " has had nothing to eat!");
        }
    }

    abstract void move();
}

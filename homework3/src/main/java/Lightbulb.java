public class Lightbulb implements Bulb{
    public Lightbulb(){}
    public void on(){
        System.out.println(this.getClass().getSimpleName() + " on");
    }
    public void off(){
        System.out.println(this.getClass().getSimpleName() + " off");
    }
}

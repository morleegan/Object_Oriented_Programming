package Part1;

public class LightBulb {
    public LightBulb(){ }
    public void on(){
        System.out.println(this.getClass().getSimpleName() + " on.");
    }
    public void off(){
        System.out.println(this.getClass().getSimpleName() + " off.");
    }
        }
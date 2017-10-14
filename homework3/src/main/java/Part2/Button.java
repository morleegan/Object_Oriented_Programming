package Part2;

public class Button  {
    private LightBulbInterface lb;

    public Button(LightBulbInterface lb){
        super();
        this.lb = lb;
    }
    public void switchOn(){
        System.out.println(this.getClass().getSimpleName() + " switched to ON");
        lb.on();
    }
    public void switchOff(){
        System.out.println(this.getClass().getSimpleName() + " switched to OFF");
        lb.off();
    }
}

package Part2;

public class PushDownButton {
    private LightBulbInterface lb;
    private int counter = 0;

    public PushDownButton(LightBulbInterface lb){
        this.lb = lb;
    }
    public void pushButton(){
        if(counter%2 == 0){
            System.out.println(this.getClass().getSimpleName() + " switched to OFF");
            lb.off();
        }
        else{
            System.out.println(this.getClass().getSimpleName() + " switched to ON");
            lb.on();
        }
        counter++;
    }
}

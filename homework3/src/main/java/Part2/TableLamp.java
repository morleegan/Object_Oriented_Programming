package Part2;

public class TableLamp {
    private LightBulb lb;
    private Button b;

    public TableLamp(LightBulb lb, Button b){
        this.lb = lb;
        this.b = b;
    }

    public void on(){
        b.switchOn();
        lb.on();
    }

    public void off(){
        b.switchOff();
        lb.off();
    }

}

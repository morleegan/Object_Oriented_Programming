public class TableLamp1 {
    //part 1 and 2 (initial make up assumed it wasn't oop)
    private Button b;
    private LightBulb l;

    public TableLamp1(Button b, LightBulb l){
        this.b = b;
        this.l = l;
    }

    public void on(){
        b.switchOn();
        l.on();
    }

    public void off(){
        b.switchOff();
        l.off();
    }

}

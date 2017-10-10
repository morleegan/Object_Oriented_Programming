public class PullButton extends Button{
    private int counter = 1;
    private LightBulb l;

    public PullButton(LightBulb l){
        super();
        this.l = l;
    }

    public void pushButton(){
        counter++;
        if(counter % 2 == 0){
            this.switchOn();
            l.on();

        }
        else{
            this.switchOff();
            l.off();
        }
    }
}

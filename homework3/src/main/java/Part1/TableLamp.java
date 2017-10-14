package Part1;

public class TableLamp {
    private LightBulb l;

    public TableLamp(LightBulb newLightBulb){
        this.l = newLightBulb;
    }
    //fastest way, without interfaces
    public void switchOn(){
        System.out.println(this.getClass().getSimpleName() + " switched to ON");
        l.on();
    }

    public  void switchOff(){
        System.out.println(this.getClass().getSimpleName() + " switched to OFF");
        l.off();
    }

}

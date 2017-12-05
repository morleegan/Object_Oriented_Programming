public class TableLamp {

    public static void main(String [] args){
        LightBulb b = new LightBulb();
        Button firstButton = new Button(b);
        firstButton.switchOn();
        firstButton.switchOff();
    }
}

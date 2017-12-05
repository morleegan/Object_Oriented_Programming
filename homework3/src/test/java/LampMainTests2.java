import Part2.TableLamp;
import Part2.Button;
import Part2.LightBulb;

public class LampMainTests2 {

    public static void main(String [] args){
        Button b = new Button();
        LightBulb lb = new LightBulb();
        TableLamp tableLamp = new TableLamp(lb, b);
        tableLamp.off();
        tableLamp.on();
    }
    
}

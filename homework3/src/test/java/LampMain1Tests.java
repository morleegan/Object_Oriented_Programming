import Part1.TableLamp;
import Part1.LightBulb;

public class LampMain1Tests {
    public static void main(String []args){
        LightBulb lb = new LightBulb();
        TableLamp buttonTest = new TableLamp(lb);

        //Part 1 and 2
        buttonTest.switchOff();
        buttonTest.switchOn();
    }
}

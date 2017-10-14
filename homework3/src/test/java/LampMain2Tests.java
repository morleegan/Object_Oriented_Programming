import Part2.Button;
import Part2.LightBulb;
import Part2.PushDownButton;

public class LampMain2Tests {
    public static void main(String [] args){
        LightBulb lb = new LightBulb();
        Button b = new Button(lb);
        b.switchOff();
        b.switchOn();

        PushDownButton pb = new PushDownButton(lb);
        pb.pushButton();
        pb.pushButton();
    }
}

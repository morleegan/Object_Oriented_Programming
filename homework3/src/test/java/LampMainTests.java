public class LampMainTests {
    public static void main(String []args){
        LightBulb lb = new LightBulb();
        Button buttonTest = new Button();

        //Part 1 and 2
        TableLamp1 tableLamp = new TableLamp1(buttonTest, lb);
        tableLamp.on();
        tableLamp.off();

    }
}

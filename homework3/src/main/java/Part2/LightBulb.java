package Part2;

public class LightBulb implements LightBulbInterface {
    public void on() {
        System.out.println(this.getClass().getSimpleName() + " on.");
    }

    public void off() {
        System.out.println(this.getClass().getSimpleName() + " off.");
    }
}

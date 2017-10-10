public class Button {

    public Button(){

    }
    public void switchOn(){
        System.out.println(this.getClass().getSimpleName() + " switched to ON");
    }
    public void switchOff(){
        System.out.println(this.getClass().getSimpleName() + " switched to OFF");
    }
}

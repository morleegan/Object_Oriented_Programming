public class TestCreature{
    private static int CREATURE_COUNT = 3;
    private static int THING_COUNT = 2;
    private static int counter = 0;

    public TestCreature(){}

    public static void main(String[] args) {
       //initialize
        Bat bat = new Bat("Batty");
        Tiger tiger = new Tiger("Tiggy");
        Ant ant = new Ant("Aunt");
        Creature[] creatureArray = {ant, bat, tiger};
        Thing[] thingArray = new Thing[THING_COUNT + CREATURE_COUNT];

        for (int i=0; i<THING_COUNT; i++) {
            thingArray[i] = new Thing("Thing" + i);
        }
        thingArray[THING_COUNT] = bat;
        thingArray[THING_COUNT+1] = tiger;
        thingArray[THING_COUNT+2] = ant;

        //Test and printing
        printLoop(thingArray);
        System.out.println('\n');
        printLoop(creatureArray);
    }

    private static void printLoop(Object[] objectArray) {
        String name = objectArray.getClass().getSimpleName(); //has [] because it's an array
        System.out.println( name.substring(0, name.length()-2)+ "s:\n");
        for(Object object: objectArray){
            System.out.println(object.toString());
            if (name.equals("Creature[]")){
                creatureActions((Creature) object);
            }
        }
    }

    private static void creatureActions(Creature creature){
        if(creature instanceof Flyer){
            ((Flyer) creature).fly();
        }
        else if(counter%2==0){
            creature.whatDidYouEat();
        }
        else if(counter%3==0){
            Thing toEat = new Thing("Eat");
            creature.eat(toEat);
        }
        else{
            creature.move();
        }
        counter =+1;
    }
}

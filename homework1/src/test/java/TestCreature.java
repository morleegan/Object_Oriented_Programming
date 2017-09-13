import org.junit.Test;

public class TestCreature{
    private static int CREATURE_COUNT = 6;
    private static int THING_COUNT = 10;
    private static boolean flag = false;

    public TestCreature(){}

    public static void main(String[] args) {
       //initialize
        Creature[] creatureArray = new Creature[CREATURE_COUNT];
        creatureArray[0] = new Fly("Harry");
        creatureArray[1] = new Bat("Black");
        creatureArray[2] = new Tiger("Stripes");
        creatureArray[3] = new Ant("Strong");
        creatureArray[4] = new Fly("Bob");
        creatureArray[5] = new Tiger("White");

        Thing[] thingArray = new Thing[THING_COUNT + CREATURE_COUNT];
        for (int i=0; i<THING_COUNT; i++) {
            thingArray[i] = new Thing("Thing" + i);
        }
        System.arraycopy(creatureArray, 0, thingArray, THING_COUNT, CREATURE_COUNT);

        //Test and printing
        printLoop(thingArray);
        printLoop(creatureArray);
    }

    private static void printLoop(Object[] objectArray) {
        String name = objectArray.getClass().getSimpleName(); //has [] because it's an array
        System.out.println( name.substring(0, name.length()-2)+ "s:\n");
        for(Object object: objectArray){
            System.out.println(object.toString());
            if (object instanceof Creature){
                creatureActions((Creature) object);
            }
        }
        System.out.println('\n');
        flag = true;
    }

    private static void creatureActions(Creature creature){
        if(creature instanceof Flyer){
            ((Flyer) creature).fly();
        }
        else{
            creature.move();
        }
        if (flag) {
            Thing toEat = new Thing("Harry");
            creature.eat(toEat);
            creature.whatDidYouEat();
        }
    }
}

public class TestCreature{
    private static int CREATURE_COUNT = 3;
    private static int THING_COUNT = 2;

    public TestCreature(){}

    public static void main(String[] args) {
       //initialize
        String className;
        Bat bat = new Bat("Batty");
        Tiger tiger = new Tiger("Tiggy");
        Ant ant = new Ant("Aunt");
        Creature[] creatureArray = {bat, tiger, ant};
        Thing[] thingArray = new Thing[THING_COUNT + CREATURE_COUNT];

        for (int i=0; i<THING_COUNT; i++) {
            thingArray[i] = new Thing("Thing" + i);
        }

        System.arraycopy(creatureArray, 0, thingArray, THING_COUNT, CREATURE_COUNT);

        //Test and printing
        System.out.println("Things:" + "\n");
        for (Thing thing : thingArray){
            System.out.println(thing.toString());

        }
        System.out.println("\n" + "Creatures:" + "\n");
        for (Thing thing : thingArray){
            className = thing.getClass().getSimpleName();
            if (!className.equals("Thing")){
                System.out.println(thing.toString());
            }
        }
    }
}

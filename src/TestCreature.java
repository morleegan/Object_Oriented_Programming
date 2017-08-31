public class TestCreature{
    private static int CREATURE_COUNT = 0;
    private static int THING_COUNT = 2;

    public TestCreature(){}

    public static void main(String[] args) {
    //        - create some Creature instances (i.e. an array of them)
    //        - create some simple Thing instances
    //        - add the Creature instances to the array of simple Thing instances
    //        - print a heading "Things:" followed by a blank line
    //        - print each thing, which each print one line about themeselves
    //        - print a blank line
    //        - print a heading "Creatures:" followed by a blank line
    //        - print each creature
    //        - print a blank line
        Thing[] thingArray = new Thing[THING_COUNT + CREATURE_COUNT];
        for (int i=0; i<THING_COUNT; i++) {
            //initialize Things
            thingArray[i] = new Thing("Thing" + i);
        }
        System.out.println("Things:" + "\n");
        for (Thing thing : thingArray){
            System.out.println(thing.toString());
        }
        System.out.println("\n" + "Creatures:" + "\n");
    }
}

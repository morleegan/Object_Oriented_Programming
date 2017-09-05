import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;

public class TigerTest {
    private Tiger eatenTiger;
    private Tiger testTiger;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp() {
        testTiger = new Tiger("Test");
        eatenTiger = new Tiger("Joe");
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp() {
        System.setOut(null);
    }

    @Test
    public void testEatsSuccess(){
        testTiger.eat(eatenTiger);
        assertSame(eatenTiger, testTiger.getInStomach());
    }

    @Test
    public void whatDidYouEatFail(){
        testTiger.whatDidYouEat();
        assertEquals(null, testTiger.getInStomach());
        assertEquals("Test Tiger has had nothing to eat!", outContent.toString().trim());
    }

    @Test
    public void whatDidYouEatSuccess(){
        testTiger.eat(eatenTiger);
        testTiger.whatDidYouEat();
        String testString[] = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("Test Tiger has eaten a Joe Tiger!", testString[1].trim());
    }

    @Test
    public void moveSuccess(){
        testTiger.move();
        assertEquals("Test Tiger has just pounced.", outContent.toString().trim());
    }

}

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static org.mockito.Mockito.*;

public class FlyTest {
    private Fly testFly;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp(){
        testFly = new Fly("Test");
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void moveSuccess(){
        Fly flySpy = spy(testFly);
        flySpy.move();
        verify(flySpy).fly();
    }

    @Test
    public void flySuccess(){
        testFly.fly();
        assertEquals("Test Fly is buzzing around in flight.", outContent.toString().trim());
    }

    @Test
    public void willEatAThing(){
        Thing isAThing = new Thing("Thing");
        Fly flySpy = spy(testFly);
        flySpy.eat(isAThing);
        verify(flySpy).eat(isAThing);
    }

    @Test
    public void willNotEatACreature(){
        Bat isACreature = new Bat("Batty");
        testFly.eat(isACreature);
        assertEquals("Test Fly won't eat a Bat", outContent.toString().trim());
    }

}

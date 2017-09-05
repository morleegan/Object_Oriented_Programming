import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;
import static org.mockito.Mockito.*;

public class BatTest {
    private Bat testBat;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp(){
        testBat = new Bat("Test");
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void moveSuccess(){
       Bat batSpy = spy(testBat);
       batSpy.move();
       verify(batSpy).fly();
    }

    @Test
    public void flySuccess(){
        testBat.fly();
        assertEquals("Test Bat is swooping through the dark.", outContent.toString().trim());
    }

}


import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

public class LightBulbTests {
    private LightBulb buttonTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void startTest(){
        buttonTest = new LightBulb();
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void onTest(){
        buttonTest.on();
        assertEquals("LightBulb on.",  outContent.toString().trim());
    }

    @Test
    public void offTest(){
        buttonTest.off();
        assertEquals("LightBulb off.", outContent.toString().trim());
    }
}


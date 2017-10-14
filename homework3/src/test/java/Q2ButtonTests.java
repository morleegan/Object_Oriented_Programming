import Part2.Button;
import Part2.LightBulb;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

public class Q2ButtonTests {
    private Button buttonTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void startTest(){
        LightBulb l = new LightBulb();
        buttonTest = new Button(l);
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void onTest(){
        buttonTest.switchOn();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("Button switched to ON",  test[0].trim());
    }

    @Test
    public void offTest(){
        buttonTest.switchOff();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("Button switched to OFF", test[0].trim());
    }
}


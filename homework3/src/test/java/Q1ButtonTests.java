import Part1.TableLamp;
import Part1.LightBulb;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

public class Q1ButtonTests {
    private TableLamp buttonTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void startTest(){
        LightBulb l = new LightBulb();
        buttonTest = new TableLamp(l);
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut( null);
    }

    @Test
    public void onTest(){
        buttonTest.switchOn();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("TableLamp switched to ON",  test[0].trim());
    }

    @Test
    public void offTest(){
        buttonTest.switchOff();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("TableLamp switched to OFF", test[0].trim());
    }
}

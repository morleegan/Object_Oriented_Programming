import Part2.PushDownButton;
import Part2.LightBulb;
import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

public class Q2PushDownButtonTests {
    private PushDownButton buttonTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void startTest(){
        LightBulb l = new LightBulb();
        buttonTest = new PushDownButton(l);
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void onTest(){
        buttonTest.pushButton();
        buttonTest.pushButton();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("PushDownButton switched to ON",  test[2].trim());
    }

    @Test
    public void offTest(){
        buttonTest.pushButton();
        String [] test = outContent.toString().split("\\r\\n|\\n|\\r");
        assertEquals("PushDownButton switched to OFF", test[0].trim());
    }
}

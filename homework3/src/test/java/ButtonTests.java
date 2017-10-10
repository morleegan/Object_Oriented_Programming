import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;

//outContent.toString().split("\\r\\n|\\n|\\r");

public class ButtonTests {
    private Button buttonTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void startTest(){
        buttonTest = new Button();
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void onTest(){
        buttonTest.switchOn();
        assertEquals("Button switched to ON",  outContent.toString().trim());
    }

    @Test
    public void offTest(){
        buttonTest.switchOff();
        assertEquals("Button switched to OFF", outContent.toString().trim());
    }
}

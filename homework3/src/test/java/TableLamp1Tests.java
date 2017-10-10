import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.mockito.Mockito.spy;
import static org.mockito.Mockito.verify;

public class TableLamp1Tests {
    private Button buttonSpy;
    private LightBulb lightBulbSpy;
    private TableLamp1 tTest;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp(){
        Button b = new Button();
        LightBulb l = new LightBulb();
        buttonSpy = spy(b);
        lightBulbSpy = spy(l);
        tTest = new TableLamp1(buttonSpy, lightBulbSpy);

        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void turnOnTest(){
        tTest.on();
        verify(buttonSpy).switchOn();
        verify(lightBulbSpy).on();
    }

    @Test
    public void turnOffTest() {
        tTest.off();
        verify(buttonSpy).switchOff();
        verify(lightBulbSpy).off();
    }

}

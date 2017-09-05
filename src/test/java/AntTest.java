import org.junit.After;
import org.junit.Before;
import org.junit.Test;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.Assert.*;

public class AntTest {
    private Ant testAnt;
    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp(){
        testAnt = new Ant("Test");
        System.setOut(new PrintStream(outContent));
    }

    @After
    public void cleanUp(){
        System.setOut(null);
    }

    @Test
    public void moveSuccess(){
        testAnt.move();
        assertEquals("Test Ant is crawling around.", outContent.toString().trim());
    }

}


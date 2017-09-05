import org.junit.Test;
import static org.junit.Assert.*;

public class ThingTest {
    @Test
    public void testNameOfThing(){
        Thing testThing = new Thing("Test");
        assertEquals("", "Test", testThing.toString());
    }
}

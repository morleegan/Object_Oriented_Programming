import org.junit.Test;

import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertNotNull;

public class ImprovedStringTokenizerTests {

    @Test
    public void ImprovedStringTokenizerIsCreated1(){
        ImprovedStringTokenizer iSTTest = new ImprovedStringTokenizer("this is a test");
        assertNotNull(iSTTest);
    }

    @Test
    public void ImprovedStringTokenizerIsCreated2(){
        ImprovedStringTokenizer iSTTest = new ImprovedStringTokenizer("this is a test", "is");
        assertNotNull(iSTTest);
    }

    @Test
    public void ImprovedStringTokenizerIsCreated3(){
        ImprovedStringTokenizer iSTTest = new ImprovedStringTokenizer("this is a test", "is", false);
        assertNotNull(iSTTest);
    }

    @Test
    public void testStringArray(){
        String [] testArray = {"this", "is", "a", "test"};
        ImprovedStringTokenizer iSTTest = new ImprovedStringTokenizer("this is a test");
        assertArrayEquals(testArray, iSTTest.stringArray());
    }

    @Test
    public void testStringTokenizer(){
        ImprovedStringTokenizer iSTTest = new ImprovedStringTokenizer("this is a test");
        assertEquals("this", iSTTest.nextToken());
    }
}

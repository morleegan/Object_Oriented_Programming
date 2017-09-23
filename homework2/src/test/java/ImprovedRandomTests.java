import org.junit.Test;

import static org.junit.Assert.assertNotNull;
import static org.junit.Assert.assertTrue;

public class ImprovedRandomTests {
    @Test
    public void ImprovedRandomIsCreated1(){
        ImprovedRandom iRTest = new ImprovedRandom();
        assertNotNull(iRTest);
    }
    @Test
    public void ImprovedRandomIsCreated2(){
        ImprovedRandom iRTest = new ImprovedRandom(100);
        assertNotNull(iRTest);
    }
    @Test
    public void RandomBetweenTest(){
        ImprovedRandom iRTest = new ImprovedRandom();
        int testVal = iRTest.rangedNext(20,100);
        assertTrue((20 < testVal) && (testVal < 100) );
    }

    @Test
    public void RandomBetweenWithSeed(){
        ImprovedRandom iRTest = new ImprovedRandom(1000);
        int testVal = iRTest.rangedNext(400, 1200);
        assertTrue((400<testVal)&&(testVal<1200));
    }
}

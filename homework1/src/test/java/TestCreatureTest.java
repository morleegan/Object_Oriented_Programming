import org.junit.Test;

import static org.mockito.Mockito.spy;

public class TestCreatureTest {
    @Test
    public void creatureActionCallsFly(){
        Fly testFly = new Fly("test");
        Fly spyFly = spy(testFly);

    }
}

public class Thing {
    public String name;

    public Thing(String name) {
        this.name = name;
    }

    public String toString() {
        // return the name of the thing
        return this.name;
    }

    public String getClassSubstring(){
        return this.getClass().toString().substring(5);
    }
}


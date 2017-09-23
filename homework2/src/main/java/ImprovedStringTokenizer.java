import java.util.StringTokenizer;

public class ImprovedStringTokenizer extends StringTokenizer{

    public ImprovedStringTokenizer(String str){
        super(str);
    }
    public ImprovedStringTokenizer(String str, String delim){
        super(str, delim);
    }
    public  ImprovedStringTokenizer(String str, String delim, boolean returnDelims){
        super(str, delim, returnDelims);
    }

    public String[] stringArray(){
        String [] strArr = new String[super.countTokens()];
        for (int i= 0; i<strArr.length; i++){
            strArr[i] = this.nextToken();
        }
        return strArr;
    }
}
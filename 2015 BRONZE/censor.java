import java.io.*;
import java.util.*;

public class censor {
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new BufferedReader(new FileReader("censor.in")));
		PrintWriter pw = new PrintWriter(new FileWriter("censor.out"));

        String s = scan.next();
        String censor = scan.next();
        // 1e6 1 * 10^6
        char[] new_s = new char[(int)1e6];
        int index = 0;
        int censorLength = censor.length();
        for (int i=0; i<s.length(); i++){
            char curChar = s.charAt(i);
            new_s[index] = curChar;
            index++;
            
            if (index<censorLength){
                continue;
            }
            boolean found = true;
            int count = 0;
            for (int j=index-censorLength; j < index; j++){
                if (new_s[j] != censor.charAt(count)){
                    found = false;
                    break;
                }
                count++;
            }
            
            if (found) {
                index -= censorLength;
            }
            
        }
        
        for (int i=0; i<index; i++){
            pw.print(new_s[i]);
        }
        scan.close();
        pw.close();
    }
}

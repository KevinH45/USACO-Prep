import java.util.*;
import java.io.*;
public class shuffleHashing{
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        
        int t = scan.nextInt();

        for (int i=0; i<t; i++){
            String p = scan.next();
            String h = scan.next();

            if (p.length() > h.length()){
                System.out.println("NO");
                continue;
            }

            boolean found = false;
            int left = 0;
            int right = p.length();
            HashMap<Character, Integer> pMap = makeMap(p);

            while (right <= h.length()){
                String substring = h.substring(left, right);
                HashMap<Character, Integer> substringMap = makeMap(substring);
                if (pMap.equals(substringMap)){
                    found = true;
                    break;
                }
                left++;
                right++;
            }

            if (found) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
        scan.close();
    }

    static HashMap<Character,Integer> makeMap(String s) {
        HashMap<Character, Integer> hash = new HashMap<>();
        for (int i=0; i<s.length(); i++){
            char curChar = s.charAt(i);
            if (hash.get(curChar) == null){
                hash.put(curChar, 1);
            } else {
                hash.put(curChar, hash.get(curChar)+1);
            }
        }
        return hash;
    }
}
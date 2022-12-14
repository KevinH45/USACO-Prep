import java.util.*;
public class perms{
    static int[] count;
    static ArrayList<String> perms = new ArrayList<>();
    static String curr = "";
    static int n;
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String s = scan.next();
        scan.close();
        n = s.length();
        count = new int[26];
        for (char c : s.toCharArray()) {
            // A : 60
            // B : 61
            // Z : 85
            //
            // count[0]
            // count[1]
            // count[25] : count Z
            count[c - 'a']++;
        }
        search();
        
        System.out.println(perms.size());
        for (String perm: perms){
            System.out.println(perm);
        }
        
    }

    public static void search() {
        if (curr.length() == n) {
            perms.add(curr);
            return;
        }
        // a_1 a_2 b_1
        // a_2 a_1 b_1

        // a b 
        
        // state: 
        //    count, perms, curr, n
        // how we do permutations with globals
        // for every possible next letter in order from A to Z
        //   // change global state
        //   // call search() recursively8
        //   // change state back


        for (int i=0; i<26; i++){
            if (count[i]==0){
                continue;
            }
            count[i]--;
            curr += ""+(char)(i+'a');
            search();
            count[i]++;

            curr = curr.substring(0,curr.length()-1); 
        }
    }

}
import java.util.*;
import java.io.*;

public class citystate{
    public static void main(String[] args) throws IOException{
        BufferedReader reader = new BufferedReader(new FileReader("citystate.in"));
		PrintWriter pw = new PrintWriter(new FileWriter("citystate.out"));
        StringTokenizer st = new StringTokenizer(reader.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        String[] cities = new String[n];
        String[] states = new String[n];
        HashMap<String, Integer> stateMap = new HashMap<>();

        for (int i=0; i<n; i++){
            st = new StringTokenizer(reader.readLine());
            cities[i] = st.nextToken().substring(0,2);
            states[i] = st.nextToken();
        }

        for (int i=0; i<n; i++){
            String key = cities[i]+states[i];
            stateMap.putIfAbsent(key, 0);
            stateMap.put(key, stateMap.get(key)+1);
        }

        int matches = 0;
        for (int i=0; i<n; i++){
            String key = states[i]+cities[i];

            if (states[i].equals(cities[i]) || !stateMap.containsKey(key)){
                continue;
            }
            // replacing the O(N) loop, you can just store the occurences in a hashmap
            // and have O(1)
            matches += stateMap.get(key);
        }

        pw.println((int)(matches/2));
        pw.close();
    }
}



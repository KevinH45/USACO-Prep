import java.util.*;
import java.io.*;
//   0  1  2  3  4  5  6  7  8  9 10 11 12 13
//               L  G     L        G
// c1 (5,inf)
// c2 (-inf,4)
public class countingliars {
    public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(System.in);

        int N = scan.nextInt();
        char[] symbols = new char[N];
        int[] positions = new int[N];
        int minLiars = Integer.MAX_VALUE;
        for (int i=0; i<N; i++){
            symbols[i] = scan.next().charAt(0);
            positions[i] = scan.nextInt();
        }

        for (int i=0; i<N; i++){
            int curPos = positions[i];
            int liarCount = 0;
            for (int j=0; j<N; j++){
                if (symbols[j]=='L' && curPos > positions[j]){
                    liarCount++;
                } else if(symbols[j]=='G' && curPos < positions[j]){
                    liarCount++;
                }
            }
            minLiars = Integer.min(minLiars, liarCount);
        }
        System.out.println(minLiars);
        scan.close();
    }
}

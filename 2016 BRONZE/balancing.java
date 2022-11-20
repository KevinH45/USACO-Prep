import java.util.*;
import java.io.*;

public class balancing {
    public static void main(String[] args) throws IOException{
        Scanner scan = new Scanner(new BufferedReader(new FileReader("balancing.in")));
		PrintWriter pw = new PrintWriter(new FileWriter("balancing.out"));

        int N = scan.nextInt();
        int B = scan.nextInt();

        int[] xVals = new int[N];
        int[] yVals = new int[N];
        for (int i=0; i<N; i++){
            xVals[i] = scan.nextInt();
            yVals[i] = scan.nextInt();
        }
        int minM = Integer.MAX_VALUE;
        // Try the one after
        for (int i=0; i<N; i++){
            int xAfter = xVals[i]+1;

            for (int s=0; s<N; s++){
                int yAfter = yVals[s]+1;
                int q1 = 0;
                int q2 = 0;
                int q3 = 0;
                int q4 = 0; 

                for (int j=0; j<N; j++){
                    if (xVals[j] < xAfter){
                        if (yVals[j] < yAfter){
                            q3++;
                        } else {
                            q2++;
                        }
                    } else {
                        if (yVals[j] < yAfter){
                            q4++;
                        } else {
                            q1++;
                        }
                    }
                }
                int curM = Math.max(Math.max(q1,q2), Math.max(q3,q4));
                minM = Math.min(curM, minM);
            }

        }

        pw.println(minM);
        pw.close();
        scan.close();
    }
}

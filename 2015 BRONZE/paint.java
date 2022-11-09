import java.io.*;
import java.util.*;

public class paint{
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new BufferedReader(new FileReader("paint.in")));
		PrintWriter pw = new PrintWriter(new FileWriter("paint.out"));

        int a = scan.nextInt();
        int b = scan.nextInt();
        int c = scan.nextInt();
        int d = scan.nextInt();

        int lower = Math.max(a, c);
        int upper = Math.min(b, d);
        int overlap = upper - lower;
        int total = d - c + b - a - Math.max(overlap, 0);

        pw.println(total);
        pw.close();
        scan.close();
    }   
}
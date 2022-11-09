// ####
// #..#
// #.##
// ....

// .#..
// .#..
// ##..
// ....

// ####
// ##..
// #..#
// ####

// ....
// .###
// .#..
// .#..
import java.util.*;
import java.io.*;

public class bcs {
    static int n;
    static int k;
    static char[][] master;
    public static void main(String[] args) throws IOException {
        Scanner scan = new Scanner(new BufferedReader(new FileReader("bcs.in")));
		PrintWriter pw = new PrintWriter(new FileWriter("bcs.out"));

        n = scan.nextInt();
        k = scan.nextInt();
        master = readPiece(scan);
        char [][][] pieces = new char[k][n][n];
        for (int i=0; i<k; i++){
            pieces[i] = readPiece(scan);
        }

        for (int i=0; i<k; i++){
            for (int j=i+1; j<k; j++){
                if (try2(pieces[i], pieces[j])) {
                    // here's where we print the answer
                    // pw.println(...);
                    pw.close();
                    scan.close();
                    return;
                }
            }
        }
    }
    static boolean try2(char[][] p1, char[][] p2){
        // *. .* .. .. ..
        // .. .. .* *. ..
        // ** ..
        // .. **
        for (int x1 = -n; x1 <= n; x1++) {
            for (int y1 = -n; y1 <= n; y1++) {
                for (int x2 = -n; x2 <= n; x2++) {
                    for (int y2 = -n; y2 <= n; y2++) {
                        // shiftPiece has to indicate somehow that we shifted out of bounds
                        char[][] sp1 = shiftPiece(p1, x1, y1);
                        char[][] sp2 = shiftPiece(p2, x2, y2);
                        // here we check for null result in sp1 or sp2

                        // here we combine the pieces and check for equality to master
                        // when we combine, we might overlapping # 
                        char[][] c = combine(sp1, sp2);

                        // check for null

                        // check if c is equal to master
                        
                    }
                }
            }
        }
        return false;
    }

    static char[][] readPiece(Scanner scan) {
        char[][] piece = new char[n][n];
        for (int j=0; j<n; j++){
            piece[j] = scan.next().toCharArray();
        }
        return piece;
    }

    static char[][] combineVert(char[][] piece1, char[][] piece2){
        return new char[4][3];
    }

    static char[][] combineHoriz(char[][] piece1, char[][] piece2){
        return new char[4][3];
    }

}

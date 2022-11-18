// Kevin Hwang, 2022
// http://www.usaco.org/index.php?page=viewproblem2&cpid=640
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
                    pw.println(String.format("%d %d", i+1, j+1));
                    pw.close();
                    scan.close();
                    return;
                }
            }
        }
        scan.close();
        pw.close();
    }
    
    static boolean try2(char[][] p1, char[][] p2){
        for (int x1 = -n; x1 <= n; x1++) {
            for (int y1 = -n; y1 <= n; y1++) {
                for (int x2 = -n; x2 <= n; x2++) {
                    for (int y2 = -n; y2 <= n; y2++) {
                        char[][] sp1 = shiftPiece(p1, x1, y1);
                        if (sp1==null){
                            continue;
                        }
                        char[][] sp2 = shiftPiece(p2, x2, y2);
                        if (sp2==null){
                            continue;
                        }

                        char[][] c = combine(sp1, sp2);

                        // check for null
                        if (c==null){
                            continue;
                        }
                        // check if c is equal to master
                        if (checkEqual(c,master)){
                            return true;
                        }
                        
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

    static boolean inBounds(int i, int j){
        return (0 <= i && i < n) && (0 <= j && j < n);
    }

    static char[][] shiftPiece(char[][] piece, int x1, int y1){
        char[][] newPiece = new char[n][n];

        // Shift
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (newPiece[i][j]!='#'){
                    newPiece[i][j] = '.';
                }
                char curChar = piece[i][j];
                
                if (curChar=='#'){
                    if (inBounds(i-y1, j+x1)){
                        newPiece[i-y1][j+x1] = '#';
                    } else {
                        return null;
                    }
                }

            }
        }

        return newPiece;
    }

    static char[][] combine(char[][] piece1, char[][] piece2){
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){

                if (piece1[i][j]=='#' && piece2[i][j]=='#'){
                    return null;
                }
                if (piece2[i][j] != '.'){
                    piece1[i][j] = piece2[i][j];
                }
            }
        }

        return piece1;
    }

    static boolean checkEqual(char[][] piece1, char[][] piece2){
        for (int i=0; i<n; i++){
            for (int j=0; j<n; j++){
                if (piece1[i][j]!=piece2[i][j]){
                    return false;
                }
            }
        }
        return true;
    }

    static void printNestedCharArr(char[][] piece){
        for(int i=0; i<piece.length; i++){
            for (int j=0; j<piece[i].length; j++){
                System.out.print(piece[i][j]);
                System.out.print(" ");
            }
            System.out.println();
        }
        System.out.println();
    }

    static void printCharArr(char[][] piece){
        for(int i=0; i<piece.length; i++){
            System.out.print(piece[i]);
            System.out.print(" ");
        }
        System.out.println();
    }
}

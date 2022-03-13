import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int sx = 0;
    static int sy = 0;
    static int r1;
    static int c1;
    static int r2;
    static int c2;
    static int max = 0;
    static int cnt = 0;
    static boolean notFinished = true;
    static int[][] map;
    static int[] dx = {0, -1, 0, 1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        r2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        map = new int[r2-r1+1][c2-c1+1];
        drawTornado();
        printTornado();
    }

    private static void printTornado() {
        int num = (int)(Math.log10(max)+1);
        for (int[] ints : map) {
            for (int anInt : ints) {
                int num2 = (int) (Math.log10(anInt) + 1);
                for (int k = 0; k < num-num2; k++) {
                    System.out.print(" ");
                }
                System.out.print(anInt + " ");
            }
            System.out.println();
        }
    }

    private static void drawTornado() {
        int k = 1;
        int d = 0;
        int n = 0;

        while (notFinished) {
            if (d == 0 || d == 2) {
                n += 1;
            }
            for (int i = 0; i < n; i++) {
                if (cnt == (r2-r1+1) * (c2-c1+1)) {
                    notFinished = false;
                    break;
                }
                if (0 <= sx-r1 && sx-r1 <= r2-r1 && 0 <= sy-c1 && sy-c1 <= c2-c1) {
                    map[sx-r1][sy-c1] = k;
                    max = Math.max(Main.max, k);
                    cnt += 1;

                }

                sx += dx[d];
                sy += dy[d];
                k += 1;
            }
            d = (d + 1) % 4;
        }
    }
}
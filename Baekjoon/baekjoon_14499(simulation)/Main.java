import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] map;
    static int n;
    static int m;
    static int x;
    static int y;
    static int k;
    static int[][] dice = new int[4][3];
    static int[] dx = {0, 0, -1, 1};
    static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        init();
        solve();

    }

    private static void solve() throws IOException {
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            int command = Integer.parseInt(st.nextToken())-1;
            move(command);

        }

    }

    private static void move(int command) {
        int nx = x + dx[command];
        int ny = y + dy[command];
        if (isNotValid(nx, ny)) {
            return;
        }

        if (command == 0) {
            int temp = dice[1][1];
            dice[1][1] = dice[1][0];
            dice[1][0] = dice[3][1];
            dice[3][1] = dice[1][2];
            dice[1][2] = temp;
        } else if (command == 1) {
            int temp = dice[1][1];
            dice[1][1] = dice[1][2];
            dice[1][2] = dice[3][1];
            dice[3][1] = dice[1][0];
            dice[1][0] = temp;
        } else if (command == 2) {
            int temp = dice[3][1];
            for (int i = 3; i > 0; i--) {
                dice[i][1] = dice[i-1][1];
            }
            dice[0][1] = temp;
        } else {
            int temp = dice[0][1];
            for (int i = 0; i < 3; i++) {
                dice[i][1] = dice[i+1][1];
            }
            dice[3][1] = temp;
        }
        x = nx;
        y = ny;

        copy();
        System.out.println(dice[1][1]);
    }

    private static void copy() {
        if (map[x][y] == 0) {
            map[x][y] = dice[3][1];
        } else {
            dice[3][1] = map[x][y];
            map[x][y] = 0;
        }
    }

    private static boolean isNotValid(int nx, int ny) {
        if (0 <= nx && nx < n && 0 <= ny && ny < m) {
            return false;
        } else {
            return true;
        }
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());
        y = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}
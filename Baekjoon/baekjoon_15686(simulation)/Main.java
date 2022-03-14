import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    static int[][] map;
    static List<Pos> people = new ArrayList<>();
    static List<Pos> chicken = new ArrayList<>();
    static boolean[] closed;
    static int answer = Integer.MAX_VALUE;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Pos {
        private int x;
        private int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        backtracking(0, -1);
        System.out.println(answer);
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int v = Integer.parseInt(st.nextToken());
                if (v == 1) {
                    people.add(new Pos(i, j));
                }
                if (v == 2) {
                    chicken.add(new Pos(i, j));
                }
                map[i][j] = v;
            }
        }
        closed = new boolean[chicken.size()];
    }

    private static void backtracking(int cnt, int idx) {
        if (cnt == chicken.size()-m) {
            answer = Math.min(answer, findMinDist());
            return;
        }

        for (int i = idx+1; i < chicken.size(); i++) {
            closed[i] = true;
            backtracking(cnt+1, i);
            closed[i] = false;
        }
    }

    private static int findMinDist() {
        int dist = 0;

        for (Pos person : people) {
            int min = Integer.MAX_VALUE;
            for (int i = 0 ; i < chicken.size(); i++) {
                if (!closed[i]) {
                    min = Math.min(min, Math.abs(person.x - chicken.get(i).x) + Math.abs(person.y - chicken.get(i).y));
                }
            }
            dist += min;
        }

        return dist;
    }
}
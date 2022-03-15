import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int answer = 0;
    static int n;
    static int m;
    static int k;
    static LinkedList<FireBall>[][] map;
    static int[] dx = {-1, -1, 0, 1, 1, 1, 0, -1};
    static int[] dy = {0, 1, 1, 1, 0, -1, -1, -1};

    static class FireBall {
        int m;
        int s;
        int d;

        public FireBall(int m, int s, int d) {
            this.m = m;
            this.s = s;
            this.d = d;
        }

        @Override
        public String toString() {
            return "FireBall{" +
                    "m=" + m +
                    ", s=" + s +
                    ", d=" + d +
                    '}';
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        solve();

    }

    private static void solve() {
        for (int i = 0; i < k; i++) {
            move();
            split();
        }
        sum();
        System.out.println(answer);
    }

    private static void sum() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j].size() >= 1) {
                    for (FireBall fireBall : map[i][j]) {
                        answer += fireBall.m;
                    }
                }
            }
        }
    }

    private static void split() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j].size() > 1) {
                    int nm = 0;
                    int ns = 0;
                    boolean odd = false;
                    boolean even = false;
                    for (FireBall fb : map[i][j]) {
                        nm += fb.m;
                        ns += fb.s;
                        if (fb.d % 2 == 1) {
                            odd = true;
                        } else {
                            even = true;
                        }
                    }

                    nm /= 5;
                    ns /= map[i][j].size();
                    map[i][j].clear();
                    for (int q = 0; q < 4; q++) {
                        if (odd && even) {
                            map[i][j].add(new FireBall(nm, ns,1+2*q));
                        } else {
                            map[i][j].add(new FireBall(nm, ns,2*q));
                        }
                    }
                }
            }
        }
    }

    private static void move() {
        LinkedList<FireBall>[][] next = new LinkedList[n][n];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                next[i][j] = new LinkedList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j].size() >= 1) {
                    for (FireBall fb : map[i][j]) {
                        int ni = Math.floorMod(i + dx[fb.d] * fb.s, n);
                        int nj = Math.floorMod(j + dy[fb.d] * fb.s, n);

                        if (fb.m != 0) {
                            next[ni][nj].addFirst(new FireBall(fb.m, fb.s, fb.d));
                        }
                    }
                }
            }
        }

        map = next;
    }

    private static void print() {
        for (LinkedList<FireBall>[] linkedLists : map) {
            for (LinkedList<FireBall> linkedList : linkedLists) {
                System.out.print(linkedList + " ");
            }
            System.out.println();
        }
        System.out.println();
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        map = new LinkedList[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                map[i][j] = new LinkedList<>();
            }
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int r = Integer.parseInt(st.nextToken())-1;
            int c = Integer.parseInt(st.nextToken())-1;
            int w = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());
            FireBall fireBall = new FireBall(w, s, d);
            map[r][c].addFirst(fireBall);
        }
    }
}
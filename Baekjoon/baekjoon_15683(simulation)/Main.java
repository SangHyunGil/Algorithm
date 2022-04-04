import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    static ArrayList<Pos> cctv = new ArrayList<>();
    static int answer = Integer.MAX_VALUE;
    static int[] dx = {1, 0, -1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Pos {
        int x;
        int y;

        public Pos(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    public static void main(String[] args) throws IOException {
        int[][] map = init();
        backtracking(0, map);
        System.out.println(answer);
    }

    private static void backtracking(int k, int[][] map) {
        if (k == cctv.size()) {
            answer = Math.min(answer, getSum(map));
            return;
        }

        Pos pos = cctv.get(k);
        int cctvNum = map[pos.x][pos.y];
        for (int i = 0; i < iterNum(cctvNum); i++) {
            int[][] copyMap = copy(map);
            move(copyMap, pos, cctvNum, i, 7);
            backtracking(k+1, copyMap);
        }
    }

    private static int[][] copy(int[][] map) {
        int[][] copyMap = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                copyMap[i][j] = map[i][j];
            }
        }
        return copyMap;
    }

    private static int iterNum(int n) {
        if (n == 1 || n == 3 || n == 4) {
            return 4;
        } else if (n == 2) {
            return 2;
        } else {
            return 1;
        }
    }

    private static void move(int[][] map, Pos pos, int cctvNum, int dir, int value) {
        if (cctvNum == 1) {
            change(map, pos, dir, value);
        } else if (cctvNum == 2) {
            change(map, pos, dir, value);
            change(map, pos, (dir+2)%4, value);
        } else if (cctvNum == 3) {
            change(map, pos, dir, value);
            change(map, pos, (dir+1)%4, value);
        } else if (cctvNum == 4) {
            change(map, pos, dir, value);
            change(map, pos, (dir+1)%4, value);
            change(map, pos, (dir+2)%4, value);
        } else if (cctvNum == 5) {
            change(map, pos, dir, value);
            change(map, pos, dir+1, value);
            change(map, pos, dir+2, value);
            change(map, pos, dir+3, value);

        }
    }

    private static void change(int[][] map, Pos pos, int dir, int value) {
        watch(map, pos, dir, value);
    }

    private static void watch(int[][] map, Pos pos, int k, int value) {
        int nx = pos.x;
        int ny = pos.y;

        while (true) {
            nx += dx[k];
            ny += dy[k];
            if (!isValid(nx, ny) || map[nx][ny] == 6) {
                return;
            }

            if (map[nx][ny] == 0) {
                map[nx][ny] = value;
            }
        }
    }

    private static boolean isValid(int nx, int ny) {
        return 0 <= nx && nx < n && 0 <= ny && ny < m;
    }

    private static int getSum(int[][] map) {
        int sum = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (map[i][j] == 0)
                    sum += 1;
            }
        }
        return sum;
    }

    private static int[][] init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[][] map = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (0 < value && value < 6) {
                    cctv.add(new Pos(i, j));
                }
                map[i][j] = value;
            }
        }
        return map;
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    static Pos robot;
    static int[][] map;
    static boolean[][] visited;
    static int answer = 0;
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};

    static class Pos {
        private int x;
        private int y;
        private int d;

        public Pos(int x, int y, int d) {
            this.x = x;
            this.y = y;
            this.d = d;
        }

        public void setX(int x) {
            this.x = x;
        }

        public void setY(int y) {
            this.y = y;
        }

        public void setD(int d) {
            this.d = d;
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        clean();
        count();
        System.out.println(answer);
    }

    private static void count() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (visited[i][j])
                    answer += 1;
            }
        }
    }

    private static void clean() {
        while (true) {
            if (!visited[robot.x][robot.y]) {
                visited[robot.x][robot.y] = true;
            }

            int cnt = 0;
            for (int i = 0; i < 4; i++) {
                rotate();
                int nx = robot.x + dx[robot.d];
                int ny = robot.y + dy[robot.d];

                if (canMove(nx, ny)) {
                    if (visited[nx][ny]) {
                        cnt += 1;
                    } else {
                        robot.setX(nx);
                        robot.setY(ny);
                        break;
                    }
                } else {
                    cnt += 1;
                }
            }
            if (cnt == 4) {
                int nd = (robot.d + 2) % 4;
                int bx = robot.x + dx[nd];
                int by = robot.y + dy[nd];

                if (canMove(bx, by)) {
                    robot.setX(bx);
                    robot.setY(by);
                } else {
                    return;
                }
            }
        }
    }

    private static boolean canMove(int nx, int ny) {
        if (map[nx][ny] == 0) {
            return true;
        } else {
            return false;
        }
    }

    private static void rotate() {
        int rotatedD = robot.d == 0 ? 3 : robot.d-1;
        robot.setD(rotatedD);
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        robot = new Pos(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));

        map = new int[n][m];
        visited = new boolean[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
    }
}
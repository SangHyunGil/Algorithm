import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int k;
    static int[][] map;
    static int l;
    static int answer;
    static Map<Integer, String> command = new HashMap<>();
    static Deque<Pos> snake = new ArrayDeque<>();
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};
    static int d = 0;

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
        move();
        System.out.println(answer);
    }

    private static void move() {
        while (true) {
            answer += 1;
            int nx = snake.getFirst().x + dx[d];
            int ny = snake.getFirst().y + dy[d];

            if (isFinished(nx, ny)) {
                return;
            }

            moveHeadAndTail(nx, ny);
            changeDirection();
        }
    }

    private static boolean isFinished(int nx, int ny) {
        if (!isValid(nx, ny))
            return true;
        if (map[nx][ny] == 2)
            return true;
        return false;
    }

    private static void moveHeadAndTail(int nx, int ny) {
        snake.addFirst(new Pos(nx, ny));
        if (map[nx][ny] == 0) {
            map[nx][ny] = 2;
            Pos pos = snake.pollLast();
            map[pos.x][pos.y] = 0;
        } else {
            map[nx][ny] = 2;
        }
    }

    private static void changeDirection() {
        if (command.containsKey(answer)) {
            String cmd = command.get(answer);
            if (cmd.equals("L")) {
                d = d == 0 ? 3 : d-1;
            } else {
                d = (d+1)%4;
            }
        }
    }

    private static boolean isValid(int i, int j) {
        if (0 <= i && i < n && 0 <= j && j < n) {
            return true;
        } else {
            return false;
        }
    }

    private static void init() throws IOException {
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        map = new int[n][n];
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken())-1;
            int y = Integer.parseInt(st.nextToken())-1;
            map[x][y] = 1;
        }

        l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            command.put(Integer.parseInt(st.nextToken()), st.nextToken());
        }
        snake.addFirst(new Pos(0, 0));
        map[0][0] = 2;
    }
}
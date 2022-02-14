import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Stream;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] direction = { {0, -1}, {-1, -1}, {-1, 0}, {-1, 1},
                                 {0, 1}, {1, 1}, {1, 0}, {1, -1}};
    static List<Cloud> cloud = new ArrayList<>();
    static int[][] graph;
    static Command[] command;
    static int n;
    static int m;

    public static class Command {
        private int dir;
        private int cnt;

        public Command(int dir, int cnt) {
            this.dir = dir;
            this.cnt = cnt;
        }

        public int getDir() {
            return this.dir;
        }

        public int getCnt() {
            return this.cnt;
        }
    }

    public static class Cloud {
        private int x;
        private int y;

        public Cloud(int x, int y) {
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public int getY() {
            return y;
        }

        public void setX(int x) {
            this.x = x;
        }

        public void setY(int y) {
            this.y = y;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Cloud)) return false;

            Cloud cloud = (Cloud) o;

            if (getX() != cloud.getX()) return false;
            return getY() == cloud.getY();
        }

        @Override
        public int hashCode() {
            int result = getX();
            result = 31 * result + getY();
            return result;
        }

        @Override
        public String toString() {
            return "Cloud{" +
                    "x=" + x +
                    ", y=" + y +
                    '}';
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        initGraph();
        initCommand();
        initCloud();

        simulate();

    }

    private static void initGraph() throws IOException {
        graph = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int v = Integer.parseInt(st.nextToken());
                graph[i][j] = v;
            }
        }
    }

    private static void initCommand() throws IOException {
        command = new Command[m];
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int dir = Integer.parseInt(st.nextToken());
            int cnt = Integer.parseInt(st.nextToken());
            command[i] = new Command(dir-1, cnt);
        }
    }

    private static void initCloud() {
        cloud.add(new Cloud(n-1, 0));
        cloud.add(new Cloud(n-1, 1));
        cloud.add(new Cloud(n-2, 0));
        cloud.add(new Cloud(n-2, 1));
    }

    private static void simulate() {
        for (Command cmd : command) {
            int dir = cmd.getDir();
            int cnt = cmd.getCnt();

            int dx = direction[dir][0];
            int dy = direction[dir][1];
            moveCloudAndRain(dx, dy, cnt);
            cloud = makeCloud();
        }

        System.out.println(getRainAmount());
    }

    private static void moveCloudAndRain(int dx, int dy, int cnt) {
        for (Cloud c : cloud) {
            c.setX(Math.floorMod(c.getX()+dx*cnt, n));
            c.setY(Math.floorMod(c.getY()+dy*cnt, n));
            rain(c);
        }

        for (Cloud c : cloud) {
            waterCopy(c);
        }
    }

    private static int getRainAmount() {
        return Arrays.stream(graph)
                .flatMapToInt(Arrays::stream)
                .reduce(Integer::sum)
                .getAsInt();
    }

    private static List makeCloud() {
        List<Cloud> newCloud = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                Cloud cd = new Cloud(i, j);
                if (graph[i][j] >= 2 && !cloud.contains(cd)){
                    newCloud.add(cd);
                    graph[i][j] -= 2;
                }
            }
        }
        return newCloud;
    }

    private static void rain(Cloud c) {
        graph[c.getX()][c.getY()] += 1;
    }

    private static void waterCopy(Cloud c) {
        int rainBasket = 0;
        for (int i = 0; i < 8; i++) {
            int nx = c.getX() + direction[i][0];
            int ny = c.getY() + direction[i][1];
            if (isValid(nx, ny) && i % 2 == 1 && graph[nx][ny] > 0) {
                rainBasket += 1;
            }
        }
        graph[c.getX()][c.getY()] += rainBasket;
    }

    private static Boolean isValid(int x, int y) {
        if (0 <= x && x < n && 0 <= y && y < n) {
            return true;
        } else {
            return false;
        }
    }
}

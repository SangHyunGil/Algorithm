import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int R;
    private static int C;
    private static int T;
    private static int[][] map;
    private static List<List<Integer>> air = new ArrayList<>();
    private static Queue<List<Integer>> dust = new LinkedList<>();
    private static int[] dx = {1, 0, -1, 0};
    private static int[] dy = {0, 1, 0, -1};

    public static void main(String[] args) throws IOException {
        init();
        while (T-- > 0) {
            findDust();
            spreadDust();
            spreadAir();
        }

        int sum = getSumOfDust();
        System.out.println(sum);

    }

    private static int getSumOfDust() {
        int sum = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] > 0)
                    sum += map[i][j];
            }
        }
        return sum;
    }

    private static void findDust() {
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (map[i][j] > 0)
                    dust.add(List.of(i, j));
            }
        }
    }

    private static void spreadDust() {
        int[][] newMap = new int[R][C];

        for (int i = 0; i < 2; i++) {
            List<Integer> a = air.get(i);
            newMap[a.get(0)][a.get(1)] = -1;
        }

        while (!dust.isEmpty()) {
            int cnt = 0;
            List<Integer> pos = dust.poll();
            int x = pos.get(0);
            int y = pos.get(1);
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (isValid(nx, ny) && map[nx][ny] != -1) {
                    cnt += 1;
                    newMap[nx][ny] += map[x][y] / 5;
                }
            }

            newMap[x][y] += map[x][y] - (map[x][y] / 5) * cnt;
        }

        map = newMap;
    }

    private static void spreadAir() {
        List<Integer> upAir = air.get(0);
        int sx1 = upAir.get(0)-1;
        int sy1 = upAir.get(1);
        while (sx1 != 0) {
            map[sx1][sy1] = map[sx1-1][sy1];
            sx1 -= 1;
        }
        while (sy1 != C-1) {
            map[sx1][sy1] = map[sx1][sy1+1];
            sy1 += 1;
        }
        while (sx1 != upAir.get(0)) {
            map[sx1][sy1] = map[sx1+1][sy1];
            sx1 += 1;
        }
        while (sy1 != upAir.get(1)+1) {
            map[sx1][sy1] = map[sx1][sy1-1];
            sy1 -= 1;
        }
        map[sx1][sy1] = 0;

        List<Integer> downAir = air.get(1);
        int sx2 = downAir.get(0)+1;
        int sy2 = downAir.get(1);

        while (sx2 != R-1) {
            map[sx2][sy2] = map[sx2+1][sy2];
            sx2 += 1;
        }
        while (sy2 != C-1) {
            map[sx2][sy2] = map[sx2][sy2+1];
            sy2 += 1;
        }
        while (sx2 != downAir.get(0)) {
            map[sx2][sy2] = map[sx2-1][sy2];
            sx2 -= 1;
        }
        while (sy2 != downAir.get(1)+1) {
            map[sx2][sy2] = map[sx2][sy2-1];
            sy2 -= 1;
        }
        map[sx2][sy2] = 0;
    }

    private static boolean isValid(int x, int y) {
        if (0 <= x && x < R && 0 <= y && y < C) {
            return true;
        } else {
            return false;
        }
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        T = Integer.parseInt(st.nextToken());

        map = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                int value = Integer.parseInt(st.nextToken());
                if (value == -1)
                    air.add(List.of(i, j, value));

                map[i][j] = value;
            }
        }
    }
}

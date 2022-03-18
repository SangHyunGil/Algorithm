import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int answer = Integer.MAX_VALUE;
    static int n;
    static int total;
    static int[][] map;
    
    public static void main(String[] args) throws IOException {
        init();
        solve();
        System.out.println(answer);
    }

    private static void solve() {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int d1 = 1; d1 <= n-i; d1++) {
                    for (int d2 = 1; d2 <= n-j; d2++) {
                        if(i + d1 + d2 >= n) continue;
                        if(j - d1 < 0 || j + d2 >= n) continue;

                        int[][] copyMap = copy(map);
                        splitArea(copyMap, i, j, d1, d2);
                    }
                }
            }
        }
    }

    private static void splitArea(int[][] copyMap, int x, int y, int d1, int d2) {
        boolean[][] visited = new boolean[n][n];
        makeEdge(x, y, d1, d2, visited);

        int[] sum = new int[5];
        for (int i = 0; i < x+d1; i++) {
            for (int j = 0; j <= y; j++) {
                if (visited[i][j]) break;
                sum[0] += map[i][j];
            }
        }

        for (int i = 0; i <= x+d2; i++) {
            for(int j = n-1; j > y; j--){
                if (visited[i][j]) break;
                sum[1] += map[i][j];
            }
        }

        for (int i = x+d1; i < n; i++) {
            for (int j = 0; j < y-d1+d2; j++) {
                if (visited[i][j]) break;
                sum[2] += map[i][j];
            }
        }

        for (int i = x+d2+1; i < n; i++) {
            for(int j = n-1; j >= y - d1 + d2; j--){
                if (visited[i][j]) break;
                sum[3] += map[i][j];
            }
        }


        sum[4] = total - (sum[0] + sum[1] + sum[2] + sum[3]);
        Arrays.sort(sum);
        answer = Math.min(answer, sum[4]-sum[0]);
    }

    private static void makeEdge(int x, int y, int d1, int d2, boolean[][] visited) {
        for (int i = 0; i <= d1; i++) {
            visited[x +i][y -i] = true;
            visited[x + d2 +i][y + d2 -i] = true;
        }

        for (int i = 0; i <= d2; i++) {
            visited[x +i][y +i] = true;
            visited[x + d1 +i][y - d1 +i] = true;
        }
    }

    private static int[][] copy(int[][] map) {
        int[][] copyMap = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                copyMap[i][j] = map[i][j];
            }
        }

        return copyMap;
    }

    private static void init() throws IOException {
        n = Integer.parseInt(br.readLine());

        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
                total += map[i][j];
            }
        }
    }
}

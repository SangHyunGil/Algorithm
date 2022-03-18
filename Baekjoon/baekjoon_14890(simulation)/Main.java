import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static Set<Integer> answer1 = new HashSet<>();
    static Set<Integer> answer2 = new HashSet<>();
    static int n;
    static int l;
    static int[][] map;
    static int[][] reverseLeftAndRightMap;
    static int[][] reverseUpsideAndDownMap;

    public static void main(String[] args) throws IOException {
        init();
        horizontalCheck(map);
        horizontalCheck(reverseLeftAndRightMap);
        verticalCheck(map);
        verticalCheck(reverseUpsideAndDownMap);
        System.out.println(answer1.size()+answer2.size());
    }

    private static void horizontalCheck(int[][] map) {
        boolean[][] visited = new boolean[n][n];
        for (int i = 0; i < n; i++) {
            boolean check = true;
            for (int j = 0; j < n-1; j++) {
                if (map[i][j] == map[i][j+1]) {
                    continue;
                } else if (map[i][j]-map[i][j+1] == 1) {
                    int nj = j+1;
                    for (int k = nj; k < nj+l; k++) {
                        if (!isValid(i, k) || visited[i][k] || map[i][k] != map[i][j+1]) {
                            check = false;
                            break;
                        }
                        visited[i][k] = true;
                    }
                } else if (map[i][j]-map[i][j+1] == -1) {
                    int nj = j+1-l;
                    for (int k = nj; k < nj+l; k++) {
                        if (!isValid(i, k) || visited[i][k] || map[i][k] != map[i][j]) {
                            check = false;
                            break;
                        }
                        visited[i][k] = true;
                    }
                } else {
                    check = false;
                    break;
                }
            }

            if (check) {
                answer1.add(i);
            }
        }
    }

    private static boolean isValid(int i, int k) {
        if (0 <= i && i < n && 0 <= k && k < n) {
            return true;
        } else {
            return false;
        }
    }

    private static void verticalCheck(int[][] map) {
        boolean[][] visited = new boolean[n][n];
        for (int j = 0; j < n; j++) {
            boolean check = true;
            for (int i = 0; i < n-1; i++) {
                if (map[i][j] == map[i+1][j]) {
                    continue;
                } else if (map[i][j]-map[i+1][j] == 1) {
                    int ni = i+1;

                    for (int k = ni; k < ni+l; k++) {
                        if (!isValid(k, j) || visited[k][j] || map[k][j] != map[i+1][j]) {
                            check = false;
                            break;
                        }
                        visited[k][j] = true;
                    }
                }  else if (map[i][j]-map[i+1][j] == -1) {
                    int ni = i+1-l;
                    for (int k = ni; k < ni+l; k++) {
                        if (!isValid(k, j) || visited[k][j] || map[k][j] != map[i][j]) {
                            check = false;
                            break;
                        }
                        visited[k][j] = true;
                    }
                } else {
                    check = false;
                    break;
                }
            }

            if (check) {
                answer2.add(j);
            }
        }
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        l = Integer.parseInt(st.nextToken());

        map = new int[n][n];
        reverseLeftAndRightMap = new int[n][n];
        reverseUpsideAndDownMap = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                int value = Integer.parseInt(st.nextToken());
                map[i][j] = value;
                reverseLeftAndRightMap[i][n-j-1] = value;
                reverseUpsideAndDownMap[n-i-1][j] = value;
            }
        }
    }
}

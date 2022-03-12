import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int m;
    static int r;
    static int[][] arr;
    static boolean[][] visited;
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {1, 0, -1, 0};

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        arr = new int[n][m];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                int value = Integer.parseInt(st.nextToken());
                arr[i][j] = value;
            }
        }

        for (int i = 0; i < r; i++) {
            rotate();
        }
        printArr();
    }

    private static void printArr() {
        StringBuilder sb = new StringBuilder();
        for (
                int y = 0;
                y < n; y++) {
            for (int x = 0; x < m; x++) {
                sb.append(arr[y][x]).append(' ');
            }
            sb.append('\n');
        }
        System.out.println(sb);
    }

    private static void rotate() {
        int i = 0;
        int j = 0;
        visited = new boolean[n][m];
        while(!visited[i][j]) {
            int k = 0;
            int ni = i;
            int nj = j;
            i += 1;
            j += 1;

            int temp = arr[ni][nj];
            for (int z = 0; z < 4; z++) {
                while (isValid(ni + dx[k], nj + dy[k]) && !visited[ni+dx[k]][nj+dy[k]]) {
                    arr[ni][nj] = arr[ni + dx[k]][nj + dy[k]];
                    visited[ni][nj] = true;

                    ni += dx[k];
                    nj += dy[k];
                }
                k += 1;
            }
            arr[i][j-1] = temp;
        }
    }

    private static boolean isValid(int ni, int nj) {
        if (0 <= ni && ni < n && 0 <= nj && nj < m) {
            return true;
        } else {
            return false;
        }
    }
}

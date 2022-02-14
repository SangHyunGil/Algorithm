import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[][] visited;
    static int answer;
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        visited = new int[n+1][m+1];
        backtracking(0);
        System.out.println(answer);
    }

    public static void backtracking(int cnt) {
        if (isFinished(cnt)) {
            answer++;
            return;
        }

        int x = cnt / m + 1;
        int y = cnt % m + 1;

        if (isSquare(x, y)) {
            backtracking(cnt+1);
        } else {
            backtracking(cnt+1);
            visited[x][y] = 1;
            backtracking(cnt+1);
            visited[x][y] = 0;
        }
    }

    private static boolean isFinished(int cnt) {
        return cnt == n * m;
    }

    public static Boolean isSquare(int x, int y) {
        if (visited[x-1][y] == 1 && visited[x][y-1] == 1 &&
            visited[x-1][y-1] == 1) {
            return true;
        } else {
            return false;
        }
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[] arr;
    static int result;
    static long[][] dp;
    
    public static void main(String[] args) throws IOException {
        init();
        solve();
        System.out.println(dp[n-2][result]);
    }

    private static void solve() {
        dp[0][arr[0]] = 1;
        for (int i = 1; i < n-1; i++) {
            for (int j = 0; j <= 20; j++) {
                if (dp[i-1][j] > 0) {
                    if (0 <= j-arr[i] && j-arr[i] <= 20){
                        dp[i][j-arr[i]] += dp[i-1][j];
                    }

                    if (0 <= j+arr[i] && j+arr[i] <= 20) {
                        dp[i][j+arr[i]] += dp[i-1][j];
                    }
                }
            }
        }
    }

    private static void init() throws IOException {
        n = Integer.parseInt(br.readLine());

        arr = new int[n-1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n-1; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        result = Integer.parseInt(st.nextToken());
        dp = new long[n][21];
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Math.max;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[][] graph;
    static int[][][] dp;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        graph = new int[n+1][n+1];
        dp = new int[n+1][n+1][3];

        for (int i = 1; i < n+1; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j < n+1; j++) {
                int temp = Integer.parseInt(st.nextToken());
                graph[i][j] = temp;
                if (temp == 0) {
                    dp[i][j][0] = 1;
                }
            }
        }

        for (int i = 1; i < n+1; i++) {
            for (int j = 1; j < n+1; j++) {
                for (int k = 0; k < 3; k++) {
                    dp[i][j][k] = max(dp[i][j][k], max(dp[i - 1][j][k], dp[i][j - 1][k]));

                    int milk = graph[i][j];
                    if (milk == k) {
                        if (dp[i - 1][j][getPrevMilk(milk)] != 0)
                            dp[i][j][milk] = max(dp[i][j][milk], dp[i - 1][j][getPrevMilk(milk)] + 1);
                        if (dp[i][j - 1][getPrevMilk(milk)] != 0)
                            dp[i][j][milk] = max(dp[i][j][milk], dp[i][j - 1][getPrevMilk(milk)] + 1);
                    }
                }
            }
        }

        System.out.println(getMaxAnswer());
    }

    private static int getMaxAnswer() {
        int ans = -Integer.MAX_VALUE;
        for (int i : dp[n][n]) {
            ans = max(ans, i);
        }
        return ans;
    }

    private static int getPrevMilk(int milk) {
        if (milk == 0) {
            return 2;
        } else if(milk == 1) {
            return 0;
        } else {
            return 1;
        }
    }
}
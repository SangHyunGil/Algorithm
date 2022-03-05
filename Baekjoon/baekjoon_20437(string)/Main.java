import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            int t = Integer.parseInt(br.readLine());

            int[] alpha = new int[26];
            for (int j = 0; j < s.length(); j++) {
                alpha[s.charAt(j)-'a'] += 1;
            }

            int min = Integer.MAX_VALUE;
            int max = 0;
            for (int j = 0; j < s.length(); j++) {
                if (alpha[s.charAt(j)-'a'] < t)
                    continue;

                int cnt = 0;
                for (int k = j; k < s.length(); k++) {
                    if (s.charAt(j) == s.charAt(k))
                        cnt += 1;

                    if (cnt == t) {
                        min = Math.min(min, k-j+1);
                        max = Math.max(max, k-j+1);
                        break;
                    }
                }
            }
            if (min == Integer.MAX_VALUE || max == 0) {
                System.out.println(-1);
            } else {
                System.out.println(min + " " + max);
            }
        }
    }
}
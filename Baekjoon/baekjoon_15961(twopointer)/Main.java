import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int[] sushi;
    private static int[] ate;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        sushi = new int[n+k-1];
        ate = new int[d+1];
        for (int i = 0; i < n; i++) {
            sushi[i] = Integer.parseInt(br.readLine());
        }

        for (int i = n; i < n+k-1; i++) {
            sushi[i] = sushi[i-n];
        }

        int answer = 0;
        int cnt = 0;
        int left = 0;
        int right = 0;
        while (left < n) {
            if (right - left < k) {
                if (ate[sushi[right]] == 0) {
                    cnt += 1;
                }
                ate[sushi[right]] += 1;
                right += 1;
            } else {
                answer = Math.max(answer, cnt + (ate[c] == 0 ? 1 : 0));
                ate[sushi[left]] -= 1;
                if (ate[sushi[left]] == 0) {
                    cnt -= 1;
                }
                left += 1;
            }
        }
        System.out.println(answer);
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {

    public static int answer = Integer.MAX_VALUE;
    public static int[] arr = new int[5];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < 5; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        solve(arr);
        System.out.println(answer);
    }

    public static void solve(int[] arr) {
        for (int i = 0; i < 5; i++) {
            for (int j = i+1; j < 5; j++) {
                int lcm1 = lcm(arr[i], arr[j]);
                for (int k = j+1; k < 5; k++) {
                    int lcm2 = lcm(lcm1, arr[k]);
                    answer = Math.min(answer, lcm2);
                }
            }
        }
    }

    public static int lcm(int a, int b) {
        return a * b / gcd(a, b);
    }

    public static int gcd(int a, int b) {
        if (b == 0)
            return a;
        return gcd(b, a % b);
    }
}

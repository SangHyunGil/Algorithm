import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[] dart;
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine());

        dart = new int[1000001];
        for (int i = 0; i < n; i++) {
            int balloon = Integer.parseInt(st.nextToken());

            if (balloon+1 < n+1 && dart[balloon+1] > 0) {
                dart[balloon+1] -= 1;
                dart[balloon] += 1;
            } else {
                dart[balloon] += 1;
            }
        }

        int sum = 0;
        for (int i : dart) {
            sum += i;
        }
        System.out.println(sum);
    }
}
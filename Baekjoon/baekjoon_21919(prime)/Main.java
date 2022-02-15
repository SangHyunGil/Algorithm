import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static Boolean[] prime;
    static Set<Integer> arr;
    static Integer length = 0;
    static Long answer = 1L;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        arr = new HashSet<>();
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            Integer num = Integer.valueOf(st.nextToken());
            arr.add(num);
            length = Math.max(length, num+1);
        }

        prime = new Boolean[length];
        Arrays.fill(prime, true);
        findPrime();

        for (int v : arr) {
            if (prime[v]) {
                answer *= v;
            }
        }

        System.out.println(answer == 1 ? -1 : answer);
    }

    private static void findPrime() {
        prime[0] = false;
        prime[1] = false;
        for (int i = 2; i*i < length; i++) {
            if (prime[i]) {
                for (int j = 2*i; j < length; j+=i) {
                    prime[j] = false;
                }
            }
        }
    }
}

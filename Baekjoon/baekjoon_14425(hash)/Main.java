import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int answer = 0;
    static int n;
    static int m;
    static Map<String, Integer> map = new HashMap<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        for (int i = 0; i < n; i++) {
            String s = br.readLine();
            map.put(s, 0);
        }

        for (int i = 0; i < m; i++) {
            String s = br.readLine();
            if (map.containsKey(s)) {
                map.put(s, map.get(s) + 1);
            }
        }

        for (Integer ans : map.values()) {
            answer += ans;
        }

        System.out.println(answer);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Map<Integer, String> map1 = new HashMap<>();
        Map<String, Integer> map2 = new HashMap<>();
        st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        for (int i = 1; i < n+1; i++) {
            String poketmon = br.readLine();
            map1.put(i, poketmon);
            map2.put(poketmon, i);
        }

        for (int i = 0; i < m; i++) {
            String request = br.readLine();
            if (request.matches("[0-9]+")) {
                System.out.println(map1.get(Integer.parseInt(request)));
            } else {
                System.out.println(map2.get(request));
            }
        }
    }
}
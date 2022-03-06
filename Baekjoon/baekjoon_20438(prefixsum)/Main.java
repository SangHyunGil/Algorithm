import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] student;
    static HashMap<Integer, Integer> sleeping = new HashMap<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int q = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        student = new int[n+3];
        Arrays.fill(student, 1);

        for (int i = 0; i < 3; i++) {
            student[i] = 0;
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            sleeping.put(Integer.parseInt(st.nextToken()), 1);
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < q; i++) {
            int attending = Integer.parseInt(st.nextToken());
            if (!sleeping.containsKey(attending)) {
                for (int j = attending; j < n + 3; j += attending) {
                    if (!sleeping.containsKey(j)) {
                        student[j] = 0;
                    }
                }
            }
        }

        for (int i = 3; i < n+3; i++) {
            student[i] += student[i-1];
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            System.out.println(student[e]-student[s-1]);
        }
    }
}
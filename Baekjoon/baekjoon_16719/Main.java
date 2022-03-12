import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static String s;
    static int[] order;
    static int k = 1;

    public static void main(String[] args) throws IOException {
        s = br.readLine();
        order = new int[s.length()];

        findOrder(0, s.length());
        printing();

    }

    private static void printing() {
        for (int i = 1; i < s.length()+1; i++) {
            String answer = "";
            for (int j = 0; j < s.length(); j++) {
                if (order[j] <= i) {
                    answer += s.charAt(j);
                }
            }
            System.out.println(answer);
        }
    }

    private static void findOrder(int s, int e) {

        if (e-s <= 0) {
            return;
        }

        int idx = findMinimum(s, e);
        order[idx] = k;
        k += 1;

        findOrder(idx+1, e);
        findOrder(s, idx);
    }

    private static int findMinimum(int start, int end) {
        char min = 'Z'+1;

        int idx = -1;
        for (int i = start; i < end; i++) {
            if (min > s.charAt(i)) {
                idx = i;
                min = s.charAt(i);
            }
        }
        return idx;
    }
}

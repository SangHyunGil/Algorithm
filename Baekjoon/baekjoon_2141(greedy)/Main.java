import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static List<Long>[] arr;
    private static long answer = -1;
    private static long diff = Long.MAX_VALUE;
    private static long right = 0;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        arr = new List[n];
        for (int i = 0; i< n; i++) {
            arr[i] = new ArrayList<>();
        }


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            long a = Integer.parseInt(st.nextToken());
            long b = Integer.parseInt(st.nextToken());
            arr[i] = new ArrayList<>(List.of(a, b));
            right += b;
        }
        Arrays.sort(arr, Comparator.comparing(a -> a.get(0)));

        long left = 0;
        for (int i = 0; i < n; i++) {
            left += arr[i].get(1);

            long candidate = Math.abs(right - left);
            if (diff > candidate) {
                answer = arr[i].get(0);
                diff = candidate;
            }
            right -= arr[i].get(1);
        }
        System.out.println(answer);
    }
}

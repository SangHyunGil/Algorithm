import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static List<Integer> arr = new ArrayList<>();
    private static List<Integer> diff = new ArrayList<>();
    private static int left = 1;
    private static int right = 0;
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        arr.add(0);
        st= new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr.add(Integer.parseInt(st.nextToken()));
        }
        arr.add(l);

        Collections.sort(arr);
        for (int i = n+1; i > 0; i--) {
            int value = arr.get(i) - arr.get(i - 1);
            diff.add(value);
            right = Math.max(right, value);
        }

        while (left <= right) {
            int mid = (left + right) / 2;

            int cnt = 0;
            for (int i = 0; i < n+1; i++) {
                cnt += (diff.get(i)-1) / mid;
            }

            if (cnt > m) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }
        System.out.println(left);
    }
}
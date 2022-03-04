import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int n;
    private static long[] arr;
    private static int l;
    private static int r;
    private static long ans = Long.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());

        arr = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Long.parseLong(st.nextToken());
        }

        Arrays.sort(arr);

        int left = 0;
        int right = n-1;

        while (left < right) {
            long value = arr[left] + arr[right];

            if (value > 0) {
                if (Math.abs(value) < ans) {
                    l = left;
                    r = right;
                    ans = Math.abs(value);
                }
                right -= 1;
            } else if (value < 0) {
                if (Math.abs(value) < ans) {
                    l = left;
                    r = right;
                    ans = Math.abs(value);
                }
                left += 1;
            } else {
                l = left;
                r = right;
                break;
            }
        }

        System.out.println(arr[l] + " " + arr[r]);
    }
}

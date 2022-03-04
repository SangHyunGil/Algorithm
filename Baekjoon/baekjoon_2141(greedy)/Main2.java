import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static List<Integer>[] arr;
    private static List<Long> sum = new ArrayList<>();
    private static long answer = -1;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());

        arr = new List[n];
        for (int i = 0; i< n; i++) {
            arr[i] = new ArrayList<>();
        }


        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            arr[i] = new ArrayList<>(List.of(a, b));
        }
        Arrays.sort(arr, Comparator.comparing(a -> a.get(0)));

        sum.add((long) arr[0].get(1));
        for (int i = 1; i < n; i++) {
            sum.add(sum.get(i-1)+arr[i].get(1));
        }

        int left = 0;
        int right = n-1;
        int answer = Integer.MAX_VALUE;

        while (left <= right) {
            int mid = (left + right) / 2;

            long leftSum = sum.get(mid);
            long rightSum = sum.get(n-1) - sum.get(mid);
            if (leftSum >= rightSum) {
                answer = Math.min(answer, arr[mid].get(0));
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        System.out.println(answer);
    }
}

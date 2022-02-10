import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

import static java.lang.Math.max;

public class Main {

    public static int answer;
    public static int n;
    public static int[] arr = new int[1001];

    public static void main(String[] args) throws IOException {
        init();

        int width = 0;
        int height = 0;
        for (int i = 0; i < 1001; i++) {
            if (arr[i] > 0) {
                width += 1;
                height = max(height, arr[i]);
            } else {
                answer += width * height;
                width = 0;
                height = 0;
            }
        }
        System.out.println(answer);
    }

    private static void init() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            for (int j = a; j < b+1; j++) {
                arr[j] += 1;
            }
        }
    }
}

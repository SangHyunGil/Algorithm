import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int x;
    static int[] arr;
    static Answer answer = new Answer(0, 0);

    static class Answer {
        int visitNum;
        int num;

        public Answer(int visitNum, int num) {
            this.visitNum = visitNum;
            this.num = num;
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        solve();
        if (answer.visitNum == 0) {
            System.out.println("SAD");
        } else {
            System.out.println(answer.visitNum);
            System.out.println(answer.num);
        }
    }

    private static void solve() {
        int start = 0;
        int end = 0;
        int sum = arr[end];
        while (end < n) {
            if (end-start == x-1) {
                if (sum > answer.visitNum) {
                    answer = new Answer(sum, 1);
                } else if (sum == answer.visitNum) {
                    answer.num += 1;
                }
                sum -= arr[start];
                start += 1;
            } else {
                end += 1;
                if (end < n) {
                    sum += arr[end];
                }
            }
        }
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        x = Integer.parseInt(st.nextToken());

        arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }
}

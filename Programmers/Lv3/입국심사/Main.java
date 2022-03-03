import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        System.out.println(solution.solution(6, new int[]{7, 10}));
    }
}
class Solution {
    public long solution(int n, int[] times) {
        long left = 0;
        long right = (long) n * times[times.length - 1];
        long answer = right;

        while (left <= right) {
            long mid = (left + right) / 2;

            long cnt = 0;
            for (int time : times) {
                cnt += mid / time;
            }

            if (cnt >= n) {
                answer = Math.min(answer, mid);
                right = mid-1;
            } else {
                left = mid+1;
            }
        }

        return answer;
    }
}
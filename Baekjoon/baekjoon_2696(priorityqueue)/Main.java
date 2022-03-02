import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int t;

    public static void main(String[] args) throws IOException {
        t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            List<Integer> answer = new ArrayList<>();
            PriorityQueue<Integer> minPq = new PriorityQueue<>();
            PriorityQueue<Integer> maxPq = new PriorityQueue<>(Comparator.reverseOrder());
            int m = Integer.parseInt(br.readLine());

            for (int j = 0; j < m; j++) {
                if (j % 10 == 0 ) {
                    st = new StringTokenizer(br.readLine());
                }

                if (maxPq.size() == minPq.size()) {
                    maxPq.add(Integer.parseInt(st.nextToken()));

                    int a = maxPq.peek();
                    int b = minPq.isEmpty() ? Integer.MAX_VALUE : minPq.peek();

                    answer.add(a > b ? b : a);
                } else {
                    int num = Integer.parseInt(st.nextToken());

                    minPq.add(num);
                }

                if (!minPq.isEmpty() && maxPq.peek() > minPq.peek()) {
                    int a = maxPq.poll();
                    int b = minPq.poll();
                    minPq.add(a);
                    maxPq.add(b);
                }
            }
            System.out.println(answer.size());
            for (int j = 0; j < answer.size(); j++) {
                if (j != 0 && j % 10 == 0) {
                    System.out.println();
                }
                System.out.print(answer.get(j) + " ");

            }
        }
    }
}
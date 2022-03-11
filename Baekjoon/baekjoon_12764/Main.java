import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    static class Period {
        private int start;
        private int duration;

        public Period(int start, int duration) {
            this.start = start;
            this.duration = duration;
        }

        public int getStart() {
            return start;
        }

        public int getDuration() {
            return duration;
        }
    }

    public static void main(String[] args) throws IOException {
        PriorityQueue<Period> pq = new PriorityQueue<>(Comparator.comparing(Period::getStart));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int duration = Integer.parseInt(st.nextToken());
            pq.add(new Period(start, duration));
        }

        int num = 0;
        int[] computer = new int[n];
        int[] count = new int[n];
        while (!pq.isEmpty()) {
            Period period = pq.poll();
            for (int i = 0; i < n; i++) {
                if (computer[i] <= period.getStart()) {
                    if (computer[i] == 0)
                        num += 1;

                    computer[i] = period.getDuration();
                    count[i] += 1;
                    break;
                }
            }
        }
        System.out.println(num);
        for (int i = 0; i < num; i++) {
            System.out.print(count[i] + " ");
        }
    }
}

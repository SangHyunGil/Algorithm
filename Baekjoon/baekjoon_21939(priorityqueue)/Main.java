import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.util.Comparator.reverseOrder;

public class Main {

    public static class Problem {
        private int rank;
        private int id;

        public Problem(int id) {
            this.id = id;
        }

        public Problem(int rank, int id) {
            this.rank = rank;
            this.id = id;
        }

        public int getRank() {
            return rank;
        }

        public int getId() {
            return id;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Problem)) return false;
            Problem problem = (Problem) o;
            return getId() == problem.getId();
        }

        @Override
        public int hashCode() {
            return Objects.hash(getId());
        }
    }

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] ranks = new int[100001];
        PriorityQueue<Problem> mpq = new PriorityQueue<>(Comparator.comparing(Problem::getRank, reverseOrder())
                .thenComparing(Problem::getId, reverseOrder()));
        PriorityQueue<Problem> lpq = new PriorityQueue<>(Comparator.comparing(Problem::getRank)
                .thenComparing(Problem::getId));

        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int id = Integer.parseInt(st.nextToken());
            int rank = Integer.parseInt(st.nextToken());
            mpq.add(new Problem(rank, id));
            lpq.add(new Problem(rank, id));
            ranks[id] = rank;
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            String cmd = st.nextToken();

            if (cmd.equals("add")) {
                int id = Integer.parseInt(st.nextToken());
                int rank = Integer.parseInt(st.nextToken());
                Problem problem = new Problem(rank, id);
                mpq.add(problem);
                lpq.add(problem);
                ranks[id] = rank;
            } else if(cmd.equals("solved")) {
                int id = Integer.parseInt(st.nextToken());
                ranks[id] = 0;
            } else {
                int num = Integer.parseInt(st.nextToken());
                Problem problem;
                if (num == 1) {
                    while (ranks[mpq.peek().getId()] != mpq.peek().getRank()) {
                        mpq.poll();
                    }
                    problem = mpq.peek();
                } else {
                    while (ranks[lpq.peek().getId()] != lpq.peek().getRank()) {
                        lpq.poll();
                    }
                    problem = lpq.peek();
                }
                sb.append(problem.getId()+"\n");
            }
        }
        System.out.println(sb);
    }
}

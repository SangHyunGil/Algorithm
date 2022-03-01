import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static int n;
    private static Map<Integer, TreeSet<Problem>> problemsByCategory = new HashMap<>();
    private static TreeSet<Problem> problems = new TreeSet<>();
    private static Map<Integer, Integer> mappingCategory = new HashMap();
    private static Map<Integer, Integer> mappingLevel = new HashMap<>();
    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static class Problem implements Comparable<Problem>{
        private int id;
        private int level;

        public Problem(int id, int level) {
            this.id = id;
            this.level = level;
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

        @Override
        public int compareTo(Problem o) {
            if (this.level == o.level) return this.id - o.id;
            else return this.level - o.level;
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int id = Integer.parseInt(st.nextToken());
            int level = Integer.parseInt(st.nextToken());
            int category = Integer.parseInt(st.nextToken());

            Problem problem = new Problem(id, level);
            TreeSet<Problem> set = problemsByCategory.getOrDefault(category, new TreeSet<>());
            set.add(problem);
            problemsByCategory.put(category, set);
            mappingCategory.put(id, category);
            mappingLevel.put(id, level);
            problems.add(problem);
        }

        int m = Integer.parseInt(br.readLine());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            String command = st.nextToken();
            if (command.equals("add")) {
                int id = Integer.parseInt(st.nextToken());
                int level = Integer.parseInt(st.nextToken());
                int category = Integer.parseInt(st.nextToken());

                Problem problem = new Problem(id, level);
                TreeSet<Problem> set = problemsByCategory.getOrDefault(category, new TreeSet<>());
                set.add(problem);
                problemsByCategory.put(category, set);
                mappingCategory.put(id, category);
                mappingLevel.put(id, level);
                problems.add(problem);
            } else if (command.equals("recommend")){
                int G = Integer.parseInt(st.nextToken());
                int x = Integer.parseInt(st.nextToken());
                if (x == 1) {
                    System.out.println(problemsByCategory.get(G).last().getId());
                } else {
                    System.out.println(problemsByCategory.get(G).first().getId());
                }

            } else if (command.equals("recommend2")){
                int x = Integer.parseInt(st.nextToken());

                if (x == 1) {
                    System.out.println(problems.last().getId());
                } else {
                    System.out.println(problems.first().getId());
                }
            } else if (command.equals("recommend3")){
                int x = Integer.parseInt(st.nextToken());
                int L = Integer.parseInt(st.nextToken());

                if (x == 1) {
                    Problem problem = problems.higher(new Problem(-1, L));
                    System.out.println(Objects.isNull(problem) ? -1 : problem.getId());
                } else {
                    Problem problem = problems.lower(new Problem(-1, L));
                    System.out.println(Objects.isNull(problem) ? -1 : problem.getId());
                }
            } else {
                int id = Integer.parseInt(st.nextToken());
                Integer category = mappingCategory.get(id);
                Integer level = mappingLevel.get(id);
                Problem problem = new Problem(id, level);

                problemsByCategory.get(category).remove(problem);
                mappingCategory.remove(id);
                problems.remove(problem);
            }
        }
    }
}
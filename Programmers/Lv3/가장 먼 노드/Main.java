import java.io.*;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        System.out.println(solution.solution(6, new int[][]{{3, 6}, {4, 3}, {3, 2}, {1, 3}, {1, 2}, {2, 4}, {5, 2}}));
    }
}

class Solution {
    int answer;
    int max;
    int[] visited;
    List<Integer>[] graph;

    public int solution(int n, int[][] edge) {
        init(n, edge);
        bfs();
        count();

        return answer;
    }

    private void count() {
        for (int i : visited) {
            if (max == i)
                answer += 1;
        }
    }

    private void bfs() {
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);

        while (!queue.isEmpty()) {
            Integer x = queue.poll();

            for (Integer nx : graph[x]) {
                if (visited[nx] == -1) {
                    visited[nx] = visited[x]+1;
                    max = Math.max(max, visited[nx]);
                    queue.offer(nx);
                }
            }
        }
    }

    private void init(int n, int[][] edge) {
        graph = new List[n+1];
        for (int i = 0; i < n +1; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] eg : edge) {
            graph[eg[0]].add(eg[1]);
            graph[eg[1]].add(eg[0]);
        }

        visited = new int[n+1];
        Arrays.fill(visited, -1);
        visited[1] = 0;
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        int[][] arr = {{3,1},{2,3},{3,4},{4,5},{4,6},{4,7},{7,8},{7,9}};
        System.out.println(solution.solution(9, arr));
    }
}

class Solution {

    List<Integer>[] graph;

    public int solution(int n, int[][] wires) {
        graph = new List[n+1];
        for (int i = 0; i < n+1; i++) {
            graph[i] = new ArrayList<>();
        }

        int answer = Integer.MAX_VALUE;
        for (int[] wire : wires) {
            graph[wire[0]].add(wire[1]);
            graph[wire[1]].add(wire[0]);
        }

        for (int[] wire : wires) {
            boolean[] visited = new boolean[n+1];
            visited[wire[0]] = true;
            visited[wire[1]] = true;
            answer = Math.min(answer, Math.abs(bfs(visited, wire[0]) - bfs(visited, wire[1])));
        }

        return answer;
    }

    private int bfs(boolean[] visited, int i) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(i);

        int cnt = 0;
        while (!queue.isEmpty()) {
            Integer x = queue.poll();

            for (Integer nx : graph[x]) {
                if (!visited[nx]) {
                    visited[nx] = true;
                    queue.add(nx);
                    cnt += 1;
                }
            }
        }

        return cnt;
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static List<Integer>[] arr;
    private static HashMap<Integer, Integer> path = new HashMap<>();
    private static boolean[] visited;
    private static int answer = 0;

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        arr = new List[n+1];
        visited = new boolean[n+1];
        for (int i = 0; i < n+1; i++) {
            arr[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            arr[a].add(b);
            arr[b].add(a);
        }

        for (int i = 0; i < n; i++) {
            Collections.sort(arr[i]);
        }

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());

        visited[s] = true;
        answer += bfs(s, e);
        Arrays.fill(visited, false);

        pathCheck(e);

        visited[s] = false;
        answer += bfs(e, s);
        System.out.println(answer);
    }

    private static void pathCheck(int e) {
        Integer temp = path.get(e);
        while (temp != null) {
            visited[temp] = true;
            temp = path.get(temp);
        }
        visited[e] = true;
    }

    private static class Node {
        int x;
        int depth;

        public Node(int x, int depth) {
            this.x = x;
            this.depth = depth;
        }

        public int getX() {
            return x;
        }

        public int getDepth() {
            return depth;
        }
    }

    private static int bfs(int s, int e) {
        Queue<Node> queue = new LinkedList<>();
        queue.add(new Node(s, 0));

        while (!queue.isEmpty()) {
            Node x = queue.poll();

            if (x.getX() == e) {
                return x.getDepth();
            }
            for (Integer nx : arr[x.getX()]) {
                if (!visited[nx]) {
                    path.put(nx, x.getX());
                    visited[nx] = true;
                    queue.add(new Node(nx, x.getDepth()+1));
                }
            }
        }
        return -1;
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static List<Integer>[] tree;
    static boolean[] visited;
    static int root;
    static int m;
    static int answer = 0;

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        visited = new boolean[n];
        st = new StringTokenizer(br.readLine());

        tree = new List[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }
        for (int i = 0; i < n; i++) {
            int parent = Integer.parseInt(st.nextToken());
            if (parent == -1) {
                root = i;
            } else {
                tree[parent].add(i);
            }
        }
        m = Integer.parseInt(br.readLine());
        if (root == m) {
            System.out.println(0);
        } else {
            remove();
            dfs(root);
            System.out.println(answer);
        }
    }

    private static void remove() {
        for (List<Integer> nodes : tree) {
            for (int i = 0; i < nodes.size(); i++) {
                if (nodes.get(i) == m) {
                    nodes.remove(i);
                    return;
                }
            }
        }
    }

    private static void dfs(int node) {
        if (tree[node].isEmpty()) {
            answer += 1;
            return;
        }

        for (Integer nd : tree[node]) {
            if (!visited[nd]) {
                visited[nd] = true;
                dfs(nd);
            }
        }
    }
}
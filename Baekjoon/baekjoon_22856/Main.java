import org.w3c.dom.Node;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[] indegree;
    static Map<Integer, Child> map = new HashMap<>();
    static Integer root;
    static Integer answer = 0;
    static Integer lastNode;

    static class Child {
        private int left;
        private int right;

        public Child(int left, int right) {
            this.left = left;
            this.right = right;
        }

        public int getLeft() {
            return left;
        }

        public int getRight() {
            return right;
        }
    }

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        indegree = new int[n+1];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());

            map.put(a, new Child(b, c));
            if (b != -1)
                indegree[b] += 1;
            if (c != -1)
                indegree[c] += 1;
        }

        for (int i = 1; i < n+1; i++) {
            if (indegree[i] == 0) {
                root = i;
                break;
            }
        }

        inorder(root);
        findLastEdgePathDist(root);
        System.out.println(answer+(n-1)*2);
    }

    private static void findLastEdgePathDist(int node) {
        while (!(node == lastNode)) {
            node = map.get(node).getRight();
            answer -= 1;
        }
    }

    private static void inorder(int node) {
        if (node == -1) {
            return;
        }

        Child child = map.get(node);
        inorder(child.getLeft());
        lastNode = node;
        inorder(child.getRight());
    }
}

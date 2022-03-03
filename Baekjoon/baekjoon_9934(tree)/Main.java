import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int size;
    private static int[] arr;
    private static List<Integer>[] tree;
    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        init(n);
        solve(0, 0, size-1);
        for (List<Integer> nodes : tree) {
            for (Integer node : nodes) {
                System.out.print(node + " ");
            }
            System.out.println();
        }
    }

    private static void solve(int depth, int s, int e) {
        if (s == e) {
            tree[depth].add(arr[s]);
            return;
        }

        int m = (s+e) / 2;
        tree[depth].add(arr[m]);
        solve(depth+1, s, m-1);
        solve(depth+1, m+1, e);
    }

    private static void init(int n) throws IOException {
        tree = new List[n];
        for (int i = 0; i < n; i++) {
            tree[i] = new ArrayList<>();
        }

        size = (int) Math.pow(2, n)-1;
        arr = new int[size];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < size; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
    }
}
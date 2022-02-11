import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

import static java.util.Comparator.comparing;
import static java.util.stream.Collectors.joining;

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;
    static int mandatoryDist;

    public static class Node {
        private int cost;
        private int x;

        public Node(int cost, int x) {
            this.cost = cost;
            this.x = x;
        }

        public int getCost() {
            return cost;
        }

        public int getX() {
            return x;
        }
    }

    public static void main(String[] args) throws IOException {
        int n = Integer.parseInt(br.readLine());
        for (int i = 0; i < n; i++) {
            sb.append(solve() + "\n");
        }
        System.out.println(sb);
    }

    private static String solve() throws IOException {
        List<Integer> answer = new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int g = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        List[] graph = getGraph(n, m, g, h);
        int[] candidate = getCandidate(t);

        for (int cd : candidate) {
            int c1 = dijkstra(graph, n,s-1,g-1) + mandatoryDist + dijkstra(graph, n, h-1, cd-1);
            int c2 = dijkstra(graph, n,s-1,h-1) + mandatoryDist + dijkstra(graph, n, g-1, cd-1);
            int c3 = dijkstra(graph, n, s-1, cd-1);

            if (Math.min(c1, c2) == c3) {
                answer.add(cd);
            }
        }

        return answer.stream()
                .sorted()
                .map(ans -> String.valueOf(ans))
                .collect(joining(" "));
    }

    private static List[] getGraph(int n, int m, int g, int h) throws IOException {
        List<Node>[] graph = new List[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            if ((a == g && b == h) || (a == h && b == g)) {
                mandatoryDist = d;
            }

            graph[a-1].add(new Node(d, b-1));
            graph[b-1].add(new Node(d, a-1));
        }

        return graph;
    }

    public static int[] getCandidate(int t) throws IOException {
        int[] candidate = new int[t];
        for (int i = 0; i < t; i++) {
            int c = Integer.parseInt(br.readLine());
            candidate[i] = c;
        }
        return candidate;
    }

    public static int dijkstra(List<Node>[] graph, int n, int s, int e) {
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[s] = 0;
        PriorityQueue<Node> pq = new PriorityQueue<>(comparing(Node::getCost));
        pq.add(new Node(0, s));

        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int cost = node.getCost();
            int x = node.getX();

            if (dist[x] < cost)
                continue;

            for (Node nd : graph[node.getX()]) {
                int ncost = nd.getCost();
                int nx = nd.getX();

                if (0 <= x && x < n && dist[nx] > ncost + cost) {
                    dist[nx] = ncost + cost;
                    pq.add(new Node(ncost+cost, nx));
                }
            }
        }
        return dist[e];
    }
}
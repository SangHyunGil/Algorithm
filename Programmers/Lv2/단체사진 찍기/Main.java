
import java.util.HashMap;

public class Main {

    private static int answer = 0;
    private static int[] visited = new int[8];
    private static HashMap<Character, Integer> people = new HashMap<>();

    public static void main(String[] args) {
        solution(2, new String[]{"N~F=0", "R~T>2"});
        System.out.println(answer);
    }

    public static int solution(int n, String[] data) {

        int answer = 0;
        init();
        solve(1, data);

        return answer;
    }

    public static void solve(int cnt, String[] data) {
        if (cnt == 8) {
            if (check(data))
                answer++;
            return;
        }

        for (int i = 0; i < 8; i++) {
            if (visited[i] == 0) {
                visited[i] = cnt;
                solve(cnt+1, data);
                visited[i] = 0;
            }
        }
    }

    private static boolean check(String[] data) {
        for (String d : data) {
            int idx1 = visited[people.get(d.charAt(0))];
            int idx2 = visited[people.get(d.charAt(2))];
            char op = d.charAt(3);
            int v = d.charAt(4) - '0' + 1;
            if (op == '=') {
                if (Math.abs(idx1-idx2) != v)
                    return false;
            } else if (op == '>') {
                if (Math.abs(idx1-idx2) <= v)
                    return false;
            } else if (op == '<') {
                if (Math.abs(idx1-idx2) >= v)
                    return false;
            }
        }

        return true;
    }

    public static void init() {
        people.put('A', 0);
        people.put('C', 1);
        people.put('F', 2);
        people.put('J', 3);
        people.put('M', 4);
        people.put('N', 5);
        people.put('R', 6);
        people.put('T', 7);
    }
}
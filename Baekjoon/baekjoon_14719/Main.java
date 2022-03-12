import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int[] arr;

    static class Point {
        private int h;
        private int w;

        public Point(int h, int w) {
            this.h = h;
            this.w = w;
        }

        public int getH() {
            return h;
        }

        public int getW() {
            return w;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());

        Point max = new Point(-1, -1);
        st = new StringTokenizer(br.readLine());
        arr = new int[w];
        for (int i = 0; i < w; i++) {
            int v = Integer.parseInt(st.nextToken());
            arr[i] = v;
            if (max.getH() < v) {
                max = new Point(v, i);
            }
        }

        int answer = 0;
        int x1 = 0;
        for (int i = 0; i < max.getW(); i++) {
            if (x1 < arr[i]) {
                x1 = arr[i];
            } else {
                answer += x1-arr[i];
            }
        }

        int x2 = 0;
        for (int i = w-1; i > max.getW(); i--) {
            if (x2 < arr[i]) {
             x2 = arr[i];
            } else {
                answer += x2-arr[i];
            }
        }
        System.out.println(answer);
    }
}

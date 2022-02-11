import java.util.*;
import java.io.*;

public class Main {

    static Info[] infos = new Info[6];
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;

    public static class Info {
        private int idx;
        private int dist;

        public Info(int idx, int dist) {
            this.idx = idx;
            this.dist = dist;
        }

        public int getIdx() {
            return idx;
        }

        public int getDist() {
            return dist;
        }
    }

    public static void main(String[] args) throws Exception {
        int k = Integer.parseInt(br.readLine());
        int n = 6;
        Info maxX = new Info(0, 0);
        Info maxY = new Info(0, 0);

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int dir = Integer.parseInt(st.nextToken());
            int dist = Integer.parseInt(st.nextToken());

            if (dir < 3) {
                maxX = updateValue(maxX, i, dist);

            } else {
                maxY = updateValue(maxY, i, dist);
            }

            infos[i] = new Info(dir, dist);
        }

        int width = Math.abs(infos[getNextIdx(maxX.getIdx())].getDist() - infos[getPrevIdx(maxX.getIdx())].getDist());
        int height = Math.abs(infos[getNextIdx(maxY.getIdx())].getDist() - infos[getPrevIdx(maxY.getIdx())].getDist());

        System.out.println((maxX.getDist()*maxY.getDist() - width*height)*k);
    }

    private static Info updateValue(Info info, int idx, int dist) {
        if (info.getDist() < dist) {
            return new Info(idx, dist);
        }
        return info;
    }

    public static int getNextIdx(int x) {
        return (x + 1) % 6;
    }

    public static int getPrevIdx(int x) {
        return (x + 5) % 6;
    }
}
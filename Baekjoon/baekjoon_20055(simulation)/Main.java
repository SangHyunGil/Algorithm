import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.StringTokenizer;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int k;
    static LinkedList<Belt> arr;
    static int zeroCnt = 0;
    static int ans = 0;

    public static class Belt {
        private int durability;
        private boolean hasRobot;

        public Belt(int durability, boolean hasRobot) {
            this.durability = durability;
            this.hasRobot = hasRobot;
        }

        public int getDurability() {
            return durability;
        }

        public boolean hasRobot() {
            return hasRobot;
        }

        public void setDurability(int durability) {
            this.durability = durability;
        }

        public void setHasRobot(boolean hasRobot) {
            this.hasRobot = hasRobot;
        }

        @Override
        public String toString() {
            return
                    durability +
                    ", " + hasRobot;
        }
    }

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        arr = new LinkedList<>();

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < 2*n; i++) {
            arr.add(new Belt(Integer.parseInt(st.nextToken()), false));
        }

        while (zeroCnt < k) {
            rotateBelt();
            moveLastRobot();
            moveRobot();
            setFirstRobot();
            moveLastRobot();
            ans += 1;
        }

        System.out.println(ans);
    }

    public static void rotateBelt() {
        arr.addFirst(arr.pollLast());
    }

    private static void moveRobot() {
        moveLastRobot();
        for (int i = n-2; i >= 0; i--) {
            Belt belt = arr.get(i);
            Belt nextBelt = arr.get(i+1);
            if (belt.hasRobot && !nextBelt.hasRobot() && nextBelt.getDurability() > 0) {
                belt.setHasRobot(false);
                nextBelt.setDurability(nextBelt.getDurability()-1);
                nextBelt.setHasRobot(true);

                if (nextBelt.getDurability() == 0) {
                    zeroCnt += 1;
                }
            }
        }
    }

    private static void setFirstRobot() {
        Belt firstBelt = arr.get(0);
        if (!firstBelt.hasRobot() && firstBelt.getDurability() > 0) {
            firstBelt.setDurability(firstBelt.getDurability()-1);
            firstBelt.setHasRobot(true);

            if (firstBelt.getDurability() == 0) {
                zeroCnt += 1;
            }
        }
    }

    private static void moveLastRobot() {
        Belt lastBelt = arr.get(n - 1);
        lastBelt.setHasRobot(false);
    }
}
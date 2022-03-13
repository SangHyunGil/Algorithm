import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int r1;
    static int c1;
    static int r2;
    static int c2;
    static int[][] map1;
    static int[][] map2;
    static int[][] map3;
    static int answer = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        init();

        int[][] rotateMap = map2;
        for (int z = 0; z < 4; z++) {
            for (int i = 0; i < map3.length- rotateMap.length; i++) {
                for (int j = 0; j < map3[0].length - rotateMap[0].length; j++) {
                    int[][] copyMap3 = copyMap(map3);
                    if (checkMap(i, j, copyMap3, rotateMap)) {
                        answer = Math.min(answer, MinSquare(copyMap3));
                    }
                }
            }
            rotateMap = rotate(rotateMap);
        }

        System.out.println(answer);
    }

    private static int MinSquare(int[][] copyMap3) {
        int x1 = Integer.MAX_VALUE;
        int x2 = Integer.MIN_VALUE;
        int y1 = Integer.MAX_VALUE;
        int y2 = Integer.MIN_VALUE;

        for (int i = 0; i < copyMap3.length; i++) {
            for (int j = 0; j < copyMap3[0].length; j++) {
                if (copyMap3[i][j] == 1) {
                    x1 = Math.min(x1, i);
                    x2 = Math.max(x2, i);
                    y1 = Math.min(y1, j);
                    y2 = Math.max(y2, j);
                }
            }
        }

        return (x2-x1+1) * (y2-y1+1);
    }

    private static boolean checkMap(int i, int j, int[][] copyMap3, int[][] rotateMap) {
        for (int q = 0; q < rotateMap.length; q++) {
            for (int p = 0; p < rotateMap[0].length; p++) {
                if (rotateMap[q][p] == 1 && copyMap3[i+q][j+p] > 0) {
                    return false;
                }
                if (rotateMap[q][p] == 1) {
                    copyMap3[i + q][j + p] = rotateMap[q][p];
                }
            }
        }
        return true;
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        r1 = Integer.parseInt(st.nextToken());
        c1 = Integer.parseInt(st.nextToken());
        map1 = new int[r1][c1];
        for (int i = 0; i < r1; i++) {
            String s = br.readLine();
            for (int j = 0; j < c1; j++) {
                int v = Integer.parseInt(String.valueOf(s.charAt(j)));
                map1[i][j] = v;
            }
        }

        st = new StringTokenizer(br.readLine());
        r2 = Integer.parseInt(st.nextToken());
        c2 = Integer.parseInt(st.nextToken());

        map2 = new int[r2][c2];
        for (int i = 0; i < r2; i++) {
            String s = br.readLine();
            for (int j = 0; j < c2; j++) {
                int v = Integer.parseInt(String.valueOf(s.charAt(j)));
                map2[i][j] = v;
            }
        }

        int max = Math.max(r2, c2);
        map3 = new int[2*max+r1][2*max+c1];
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c1; j++) {
                map3[i+max][j+max] = map1[i][j];
            }
        }
    }

    private static int[][] rotate(int[][] m) {
        int N = m.length;
        int M = m[0].length;
        int[][] copyMap = new int[M][N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                copyMap[j][N-1-i] = m[i][j];
            }
        }
        return copyMap;
    }

    private static int[][] copyMap(int[][] m) {
        int N = m.length;
        int M = m[0].length;
        int[][] copyMap = new int[N][M];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                copyMap[i][j] = m[i][j];
            }
        }
        return copyMap;
    }
}
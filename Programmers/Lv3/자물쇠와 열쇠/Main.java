import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {

        Solution solution = new Solution();
        System.out.println(solution.solution(new int[][]{{0, 0, 0}, {1, 0, 0}, {0, 1, 1}},
                          new int[][]{{1, 1, 1}, {1, 1, 0}, {1, 0, 1}}));
    }
}

class Solution {
    int n;
    int m;
    int[][] realKey;
    int[][] realLock;

    public boolean solution(int[][] key, int[][] lock) {

        n = key.length;
        m = lock.length;
        realKey = key;

        for (int z = 0; z < 4; z++) {
            for (int i = -20; i <= 20; i++) {
                for (int j = -20; j <= 20; j++) {
                    realLock = copy(lock);
                    if (isPossible(i, j)) {
                        return true;
                    }
                }
            }
            realKey = rotate(realKey);
        }

        return false;
    }

    private boolean isPossible(int p, int q) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (realKey[i][j] == 0) continue;
                int ni = i+p;
                int nj = j+q;
                if (notValid(ni, nj)) continue;
                if (realLock[ni][nj] == 1 && realKey[i][j] == 1) {
                    return false;
                }

                realLock[ni][nj] = 1;
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                if (realLock[i][j] == 0)
                    return false;
            }
        }
        return true;
    }

    private boolean notValid(int ni, int nj) {
        if (0 <= ni && ni < m && 0 <= nj && nj < m) {
            return false;
        } else {
            return true;
        }
    }

    private int[][] copy(int[][] map) {
        int[][] copyMap = new int[m][m];

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < m; j++) {
                copyMap[i][j] = map[i][j];
            }
        }
        return copyMap;
    }

    private int[][] rotate(int[][] map) {
        int[][] copyMap = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                copyMap[j][n-i-1] = map[i][j];
            }
        }
        return copyMap;
    }
}
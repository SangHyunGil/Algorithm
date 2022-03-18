import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static int n;
    static int[] num = {4, 7};
    static String s = "";

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        print(makePattern());
    }

    private static void print(String pattern) {
        String s = "";

        for (int i = 0; i < pattern.length(); i++) {
            s += num[Integer.parseInt(String.valueOf(pattern.charAt(i)))];
        }

        System.out.println(s);
    }

    public static String makePattern() {
        String binary = "";
        int newN = n+1;
        while (newN > 0) {
            int m = newN % 2;
            binary = m + binary;

            newN /= 2;
        }
        return binary.substring(1);
    }
}
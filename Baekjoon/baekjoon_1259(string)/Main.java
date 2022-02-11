import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import static java.util.Comparator.comparing;

public class Main {
    static String s1;
    static String s2;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static StringTokenizer st;

    public static void main(String[] args) throws IOException {

        while(true) {
            st = new StringTokenizer(br.readLine());
            String pd = st.nextToken();
            if (pd.equals("0"))
                break;

            int mid = pd.length() / 2;
            if (pd.length() % 2 == 0) {
                s1 = pd.substring(0, mid);
                s2 = pd.substring(mid);
            } else {
                s1 = pd.substring(0, mid);
                s2 = pd.substring(mid + 1);
            }
            sb.append(getAnswer(s1.equals(reverse(s2))) + "\n");
        }
        System.out.println(sb);
    }

    public static String getAnswer(Boolean isSame) {
        return isSame ? "yes" : "no";
    }

    public static String reverse(String s) {
        String ns = "";
        for (int i = s.length()-1; i >= 0; i--) {
            ns += s.charAt(i);
        }
        return ns;
    }
}
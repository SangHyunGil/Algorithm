import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static String html;


    public static void main(String[] args) throws IOException {
        html = br.readLine();
        findDivTags();
        System.out.println(sb);
    }

    private static void findDivTags() {
        Pattern dPattern = Pattern.compile("(?<=<div\\s)(.*?)(?=</div>)");
        Matcher dMatcher = dPattern.matcher(html);
        while(dMatcher.find()) {
            String s = dMatcher.group();
            findTitle(s);
            Pattern pPattern = Pattern.compile("<p>.*?</p>");
            Matcher pMatcher = pPattern.matcher(s);
            while(pMatcher.find()) {
                String p = pMatcher.group();

                String temp = "";
                String[] split = p.split("<(/)?[a-z]+(\\s)?>");
                for (String s1 : split) {
                    if (!s1.isEmpty())
                        temp += s1;
                }
                temp = temp.trim();
                temp = temp.replaceAll("\\s+", " ");
                sb.append(temp + "\n");
            }
        }
    }

    private static void findTitle(String s) {
        Pattern tPattern = Pattern.compile("(?<=title=\").+(?=\")");
        Matcher tMatcher = tPattern.matcher(s);
        tMatcher.find();
        String title = tMatcher.group();
        sb.append("title : " + title + "\n");
    }
}
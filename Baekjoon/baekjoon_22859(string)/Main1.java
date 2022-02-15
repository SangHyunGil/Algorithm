import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringBuilder sb = new StringBuilder();
    static String html;


    public static void main(String[] args) throws IOException {
        html = br.readLine();
        deleteMainSyntax();
        splitDivSyntax();
        System.out.println(sb);
    }

    private static void splitDivSyntax() {
        String[] split = html.split("</div>");
        for (String s : split) {
            extract(s);
        }
    }

    private static void extract(String s) {
        String[] tag = s.split("<(/)?p>");
        extractTitle(tag[0]);
        for (int i = 1; i < tag.length; i++) {
            if (!tag[i].isEmpty())
                extractSentence(tag[i]);
        }
    }

    private static void extractSentence(String tag) {
        String[] word = tag.split("<(/)?[a-z]+(\\s)?>");
        String store = "";
        for (int i = 0; i < word.length; i++) {
                store += word[i];
        }
        String trimS = store.trim();
        String ns = trimS.replaceAll("\\s+", " ");
        sb.append(ns + "\n");
    }

    private static void extractTitle(String s) {
        sb.append("title : " + s.substring(12, s.length()-2).trim() + "\n");
    }

    private static void deleteMainSyntax() {
        html = html.substring(6, Main.html.length() - 7);
    }
}
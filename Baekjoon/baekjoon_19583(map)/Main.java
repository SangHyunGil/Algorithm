import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static int ans = 0;
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static StringTokenizer st;
    static HashMap<String, ArrayList<Integer>> record = new HashMap<>();

    public static void main(String[] args) throws IOException {
        st = new StringTokenizer(br.readLine(), " ");
        int startMeetingMinutes = convertToMinutes(st.nextToken());
        int endMeetingMinutes = convertToMinutes(st.nextToken());
        int endStreamingMinutes = convertToMinutes(st.nextToken());

        String input;
        while ((input = br.readLine()) != null) {
            st = new StringTokenizer(input, " ");
            int minutes = convertToMinutes(st.nextToken());
            String nickname = st.nextToken();
            ArrayList<Integer> arr = record.getOrDefault(nickname, new ArrayList<>());
            arr.add(minutes);
            record.put(nickname, arr);
        }

        for (String nick : record.keySet()) {
            Boolean enter = false;
            Boolean exit = false;
            for (Integer minute : record.get(nick)) {
                if (minute <= startMeetingMinutes) {
                    enter = true;
                } else if (minute >= endMeetingMinutes && minute <= endStreamingMinutes) {
                    exit = true;
                }
            }

            if (enter && exit) {
                ans += 1;
            }
        }
        System.out.println(ans);
    }

    public static int convertToMinutes(String s) {
        String[] clock = s.split(":");
        int minutes = 0;
        minutes += Integer.parseInt(clock[0]) * 60;
        minutes += Integer.parseInt(clock[1]);
        return minutes;
    }
}
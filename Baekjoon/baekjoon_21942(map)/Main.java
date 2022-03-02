import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.*;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;
    private static int n;
    private static int period;
    private static int cost;
    private static HashMap<Record, LocalDateTime> record = new HashMap<>();
    private static HashMap<String, Long> costRecord = new HashMap<>();

    public static class Record {
        private String person;
        private String machine;

        public Record(String person, String machine) {
            this.person = person;
            this.machine = machine;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Record)) return false;
            Record record = (Record) o;
            return Objects.equals(person, record.person) && Objects.equals(machine, record.machine);
        }

        @Override
        public int hashCode() {
            return Objects.hash(person, machine);
        }
    }

    public static void main(String[] args) throws IOException {
        init();
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            LocalDateTime localDateTime = getLocalDateTime();
            String machine = st.nextToken();
            String person = st.nextToken();

            Record newRecord = new Record(person, machine);
            if (!Main.record.containsKey(newRecord)) {
                Main.record.put(newRecord, localDateTime);
            } else {
                LocalDateTime prevLocalDateTime = Main.record.get(newRecord);
                long borrowMinutes = Duration.between(prevLocalDateTime, localDateTime).toMinutes();
                if (isOverDue(borrowMinutes)) {
                    long penalty = calcPenalty(borrowMinutes);
                    Long prevPenalty = costRecord.getOrDefault(person, 0L);
                    costRecord.put(person, prevPenalty+penalty);
                }
                Main.record.remove(newRecord);
            }
        }
        if (costRecord.isEmpty()) {
            System.out.println(-1);
        } else {
            ArrayList<String> keys = new ArrayList<>(costRecord.keySet());
            Collections.sort(keys);
            for (String key : keys) {
                System.out.println(key + " " + costRecord.get(key));
            }
        }
    }

    private static long calcPenalty(long borrowMinutes) {
        return (borrowMinutes - period) * cost;
    }

    private static boolean isOverDue(long borrowMinutes) {
        return (borrowMinutes - period) > 0;
    }

    private static LocalDateTime getLocalDateTime() {
        String[] date = st.nextToken().split("-");
        LocalDate localDate = LocalDate.of(Integer.parseInt(date[0]), Integer.parseInt(date[1]), Integer.parseInt(date[2]));
        String[] time = st.nextToken().split(":");
        LocalTime localTime = LocalTime.of(Integer.parseInt(time[0]), Integer.parseInt(time[1]));
        return LocalDateTime.of(localDate, localTime);
    }

    private static void init() throws IOException {
        st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        period = getPeriod();
        cost = Integer.parseInt(st.nextToken());
    }

    private static int getPeriod() {
        String[] s = st.nextToken().split("/");
        int day = Integer.parseInt(s[0]);
        String[] hourAndMinute = s[1].split(":");
        int hour = Integer.parseInt(hourAndMinute[0]);
        return Integer.parseInt(hourAndMinute[1]) + hour * 60 + day * 24 * 60;
    }
}
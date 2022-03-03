import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Main {

    private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    private static StringTokenizer st;

    public static void main(String[] args) throws IOException {
        Solution solution = new Solution();
        System.out.println(solution.solution(new String[]{"2016-09-15 01:00:04.001 2.0s",
                "2016-09-15 01:00:07.000 2s"}));
    }
}

class Solution {
    class Interval {

        private static final double TERM = 0.999;

        private double from;
        private double to;

        public Interval(double from, double to) {
            this.from = from;
            this.to = to;
        }

        public double getTo() {
            return to;
        }

        public boolean exist(double x) {
            if (x+TERM <= from || to < x)
                return false;
            else
                return true;
        }
    }

    int start;
    int end;
    int answer;

    public int solution(String[] lines) {
        Interval[] intervals = new Interval[lines.length];

        for (int i = 0; i < lines.length; i++) {
            String[] timeline = lines[i].split(" ");
            double time = getTime(timeline[1]);
            double term = Double.parseDouble(timeline[2].substring(0, timeline[2].length()-1));

            if (i == 0) {
                start = (int) (time-term);
            } else if (i == lines.length-1) {
                end = (int) time;
            }
            Interval interval = new Interval(time - term, time);
            intervals[i] = interval;
        }

        List<Double> endTime = Arrays.stream(intervals).
                map(Interval::getTo)
                .collect(Collectors.toList());
        for (Double eTime : endTime) {
            int cnt = 0;
            for (Interval interval : intervals) {
                if (interval.exist(eTime)) {
                    cnt += 1;
                }
            }
            answer = Math.max(answer, cnt);
        }

        return answer;
    }

    private double getTime(String s) {
        String[] time = s.split(":");
        int hour = Integer.parseInt(time[0]);
        int minute = Integer.parseInt(time[1]);
        double second = Double.parseDouble(time[2]);
        return hour * 60 * 60 + minute * 60 + second;
    }
}
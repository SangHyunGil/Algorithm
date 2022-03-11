import java.io.IOException;
import java.util.*;
import java.util.stream.Collectors;

class Solution {

    public class Genres {
        private String name;
        private Integer sumPlays = 0;

        public Genres(String name) {
            this.name = name;
        }

        public void addPlay(int play) {
            this.sumPlays += play;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (!(o instanceof Genres)) return false;
            Genres genres = (Genres) o;
            return Objects.equals(name, genres.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name);
        }

        @Override
        public String toString() {
            return "Genres{" +
                    "name='" + name + '\'' +
                    ", sumPlays=" + sumPlays +
                    '}';
        }
    }

    public class Play {
        private int play;
        private int index;

        public Play(int play, int index) {
            this.play = play;
            this.index = index;
        }

        public int getPlay() {
            return play;
        }

        public int getIndex() {
            return index;
        }

        @Override
        public String toString() {
            return "Play{" +
                    "play=" + play +
                    ", index=" + index +
                    '}';
        }
    }

    public int[] solution(String[] genres, int[] plays) {

        Map<Genres, Integer> order = new HashMap<>();
        Map<Genres, PriorityQueue<Play>> map = new HashMap<>();

        for (int i = 0; i < genres.length; i++) {
            Genres gr = new Genres(genres[i]);
            PriorityQueue<Play> play = map.getOrDefault(gr, new PriorityQueue<>(Comparator.comparing(Play::getPlay).reversed().thenComparing(Play::getIndex)));
            Integer sum = order.getOrDefault(gr, 0);
            play.add(new Play(plays[i], i));
            sum += plays[i];
            map.put(gr, play);
            order.put(gr, sum);

        }


        List<Genres> key = order.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByValue(Comparator.reverseOrder()))
                .map(Map.Entry::getKey)
                .collect(Collectors.toList());

        ArrayList<Integer> ans = new ArrayList<>();
        for (Genres g : key) {
            PriorityQueue<Play> p = map.get(g);
            for (int i = 0; i < 2; i++) {
                if (!p.isEmpty()) {
                    ans.add(p.poll().getIndex());
                }
            }
        }
        return ans.stream().mapToInt(i -> i).toArray();
    }
}
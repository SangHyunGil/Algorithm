import java.util.*;

 

class Solution {

    public int[] solution(int[] lottos, int[] win_nums) {

        int ans = 0;

        int count_0 = 0;

        int[] answer = new int[2];

        int[] orders = {6, 6, 5, 4, 3, 2, 1};

        Map<Integer, Boolean> map = new HashMap<>();

        for (int lotto : lottos) {

            if (lotto == 0) {

                count_0 += 1;

                continue;

            }

            map.put(lotto, true);

        }

        

        for (int win_num : win_nums)

            if (map.containsKey(win_num))

                ans += 1;

        

        answer[0] = orders[ans+count_0];

        answer[1] = orders[ans];

        

        return answer;

    }

}
package PGM.Lv3.양과늑대;

import java.util.*;

public class Solution {

    List<List<Integer>> grassLand = new ArrayList<>();
    int maxSheep;
    int[] _info;

    public int solution(int[] info, int[][] edges) {
        _info = info;
        for (int i = 0; i < info.length; i++) {
            grassLand.add(new ArrayList<>());
        }

        for (int[] edge : edges) {
            grassLand.get(edge[0])
                     .add(edge[1]);
        }

        dfs(0, new int[]{0, 0}, new ArrayList<>());
        return maxSheep;
    }

    public void dfs(int now, int[] state, List<Integer> queue) {
        state[_info[now]] += 1;
        maxSheep = Math.max(maxSheep, state[0]);
        if (state[0] <= state[1]) return;

        queue.addAll(grassLand.get(now));
        for (int i = 0; i < queue.size(); i++) {
            int next = queue.get(i);
            queue.remove(i);
            dfs(next, Arrays.copyOf(state, 2), queue);
            queue.add(i, next);
        }
        queue.removeAll(grassLand.get(now));
    }
}
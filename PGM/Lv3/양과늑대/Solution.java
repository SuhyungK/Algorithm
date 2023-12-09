package PGM.Lv3.양과늑대;

import java.util.*;

public class Solution {

    // 2진 트리 모양 초원 정보
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
        // state : [양의 개수, 늑대의 개수]
        state[_info[now]] += 1;
        maxSheep = Math.max(maxSheep, state[0]);

        // 양의 개수 = 늑대의 개수면 늑대가 양을 다 잡아먹기 때문에 return 
        if (state[0] <= state[1]) return;
        
        // 현재 노드의 자식 노드들을 큐에 전부 추가
        queue.addAll(grassLand.get(now));
        for (int i = 0; i < queue.size(); i++) {
            int next = queue.get(i);
            queue.remove(i);
            dfs(next, Arrays.copyOf(state, 2), queue);
            queue.add(i, next);
        }
        // 
        queue.removeAll(grassLand.get(now));
    }
}
package PGM.Lv3.섬연결하기;

import java.util.*;

public class Solution {
    static int[] parent;
    public int solution(int n, int[][] costs) {
        parent = new int[n];
        for (int i = 1; i < n; i++) {
            parent[i] = i;
        }
        Arrays.sort(costs, (o1, o2) -> {
            return o1[2] - o2[2];
        });

        int answer = 0;
        for (int[] cur : costs) {
            if (find(cur[0]) != find(cur[1])) {
                union(cur[0], cur[1]);
                answer += cur[2];
            }
        }

        return answer;
    }

    int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }

        return parent[x];
    }

    void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x <= y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }
}
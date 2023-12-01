package PGM.Lv2.카카오프렌즈컬러링북;

import java.util.LinkedList;
import java.util.Queue;

public class Solution {
    public int[] solution(int m, int n, int[][] picture) {
        int[] answer = new int[2];
        boolean[][] visited = new boolean[m][n];
        int[][] direction = new int[][] {{0, -1}, {1, 0}, {-1, 0}, {0, 1}};
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (picture[i][j] == 0 || visited[i][j]) continue;
                answer[0]++;
                visited[i][j] = true;

                Queue<int[]> queue = new LinkedList<>();
                queue.add(new int[] {i, j});
                int colorSize = 1;
                while (!queue.isEmpty()) {
                    int[] q = queue.poll();

                    int curX = q[0];
                    int curY = q[1];
                    int p = picture[i][j];

                    for (int k = 0; k < 4; k++) {
                        int nextX = curX + direction[k][0];
                        int nextY = curY + direction[k][1];

                        if (!(-1 < nextX && nextX < m && -1 < nextY && nextY < n && !visited[nextX][nextY] && picture[nextX][nextY] == p)) continue;
                        colorSize++;
                        queue.add(new int[] {nextX, nextY});
                        visited[nextX][nextY] = true;
                    }
                }
                answer[1] = Math.max(answer[1], colorSize);
            }
        }

        return answer;
    }
}

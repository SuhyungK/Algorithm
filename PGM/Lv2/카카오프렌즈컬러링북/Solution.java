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

                    int ii = q[0];
                    int jj = q[1];
                    int p = picture[i][j];

                    for (int k = 0; k < 4; k++) {
                        int ni = ii + direction[k][0];
                        int nj = jj + direction[k][1];

                        if (!(-1 < ni && ni < m && -1 < nj && nj < n && !visited[ni][nj] && picture[ni][nj] == p)) continue;
                        colorSize++;
                        queue.add(new int[] {ni, nj});
                        visited[ni][nj] = true;
                    }
                }
                answer[1] = Math.max(answer[1], colorSize);
            }
        }

        return answer;
    }
}

// Bad Grass

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

class Crd {
    int x;
    int y;

    Crd(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

public class baekjoon_6080 {
    static int R;
    static int C;
    static int[][] grass;
    static int[][] direction = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}, {-1, 1}, {1, -1}, {1, 1}, {-1, -1}};

    static void bfs(int startX, int startY) {
        Queue<Crd> queue = new LinkedList<>();
        queue.add(new Crd(startX, startY));

        while (!queue.isEmpty()) {
            Crd cur = queue.poll();

            for (int[] ints : direction) {
                Crd next = new Crd(cur.x + ints[0], cur.y + ints[1]);
                if (next.x < 0 || next.y < 0 || next.x >= R || next.y >= C || grass[next.x][next.y] == 0) continue;

                grass[next.x][next.y] = 0;
                queue.add(next);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        R = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());

        grass = new int[R][C];
        for (int i = 0; i < R; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < C; j++) {
                grass[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int answer = 0;
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                if (grass[i][j] == 0) continue;
                answer++;
                grass[i][j] = 0;
                bfs(i, j);
            }
        }
        System.out.println(answer);
    }
}
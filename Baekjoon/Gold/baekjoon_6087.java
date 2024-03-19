// 레이저 통신

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

class Pos implements Comparable<Pos>{
    int x, y, d, count;

    public Pos(int x, int y, int d, int count) {
        this.x = x;
        this.y = y;
        this.d = d;
        this.count = count;
    }

    @Override
    public int compareTo(Pos o) {
        return this.count - o.count;
    }

}

public class baekjoon_6087 {
    static char[][] MAP;
    static int W;
    static int H;
    static int[][] dir = new int[][] {{1, 0}, {0, -1}, {-1, 0}, {0, 1}};
    static int[][][] mirror;

    static Pos findStart() {
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (MAP[i][j] == 'C') {
                    MAP[i][j] = '.';
                    return new Pos(i, j, -1, 0);
                }
            }
        }
        return null;
    }

    public static int findC(Pos now) {
        PriorityQueue<Pos> pq = new PriorityQueue<>();
        pq.add(now); 
        Pos cur;
        while (!pq.isEmpty()) {
            cur = pq.poll();

            // System.out.println();
            // for (int i = 0; i < H; i++) {
            //     System.out.println(Arrays.toString(mirror[i]));
            // }

            if (MAP[cur.x][cur.y] == 'C') {
                return cur.count;
            }

            for (int i = 0; i < 4; i++) {
                // 다음에 이동할 위치 찾기
                int nextX = cur.x + dir[i][0];
                int nextY = cur.y + dir[i][1];

                if (nextX < 0 || nextX >= H || nextY < 0 || nextY >= W || MAP[nextX][nextY] == '*') continue;
                
                if (cur.d != i && cur.d != -1) {
                    if (mirror[nextX][nextY][i] > cur.count + 1) {
                        mirror[nextX][nextY][i] = cur.count + 1;
                        pq.add(new Pos(nextX, nextY, i, cur.count + 1));
                    }
                } else {
                    if (mirror[nextX][nextY][i] > cur.count) {
                        mirror[nextX][nextY][i] = cur.count;
                        pq.add(new Pos(nextX, nextY, i, cur.count));
                    }
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        W = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        MAP = new char[H][W];
        for (int i = 0; i < H; i++) {
            MAP[i] = br.readLine().toCharArray();
        }

        mirror = new int[H][W][4];
        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                Arrays.fill(mirror[i][j], Integer.MAX_VALUE);
            }
        }

        System.out.println(findC(findStart()));
    }
}
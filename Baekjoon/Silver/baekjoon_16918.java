// 봄버맨

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_16918 {
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int R = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());

        String[][] arr = new String[R][C];
        for (int i = 0; i < R; i++) {
            String[] rowInput = br.readLine().split("");
            for (int j = 0; j < C; j++) {
                arr[i][j] = rowInput[j];
            }
        }

        int[] dx = new int[] {-1, 0, 1, 0};
        int[] dy = new int[] {0, 1, 0, -1};
        N--;
        Queue<int[]> queue = new LinkedList<>();
        while (N > 0) {
            // 1. 모든 칸에 폭탄 설치
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if (arr[i][j].equals(".")) {
                        arr[i][j] = "O";
                    } else {
                        queue.add(new int[] {i, j});
                    }
                }
            }
            N--;
            if (N <= 0) break;

            // 2. 1초가 지나고 모든 폭탄 터짐
            while (!queue.isEmpty()) {
                int[] pos = queue.poll();
                int x = pos[0];
                int y = pos[1];
                
                arr[x][y] = ".";
                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];
                    
                    if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
                    arr[nx][ny] = ".";
                }
            }
            N--;
        }
        
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }   
}

// 벽 부수고 이동하기 4

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_16946 {
    static int[][] direction = new int[][] {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
    static int bfs(int[][] map, int x, int y, int number) {
        int[] cur;
        int nextX; 
        int nextY;
        int count = 1;
        Queue<int[]> queue = new LinkedList<>();
        map[x][y] = number;
        queue.add(new int[] {x, y});
        while (!queue.isEmpty()) {
            cur = queue.poll();

            for (int i = 0; i < 4; i++) {
                nextX = cur[0] + direction[i][0];
                nextY = cur[1] + direction[i][1];

                if (nextX < 0 || nextX >= map.length || nextY < 0 || nextY >= map[0].length || map[nextX][nextY] != 0) {
                    continue;
                } 

                map[nextX][nextY] = number;
                count++;
                queue.add(new int[] {nextX, nextY});
            }
        }

        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] map = new int[N][M];
        String[] inputLine;
        for (int i = 0; i < N; i++) {
            inputLine = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                map[i][j] = Integer.parseInt(inputLine[j]);
            }
        }

        Map<Integer, Integer> moveCount = new HashMap();
        int number = 2;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) {
                    moveCount.put(number, bfs(map, i, j, number));
                    number++;
                }
            }
        }

        moveCount.put(1, 0);
        int[][] answer = new int[N][M];
        StringBuilder sb = new StringBuilder();
        Set<Integer> set;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 1) {
                    set = new HashSet<>();
                    answer[i][j] = 1;
                    for (int k = 0; k < 4; k++) {
                        int ni = i + direction[k][0];
                        int nj = j + direction[k][1];

                        if (ni < 0 || ni >= N || nj < 0 || nj >= M) {
                            continue;
                        }
                        
                        set.add(map[ni][nj]);
                    }

                    System.out.println(i + " " + j + " " + set);

                    for (Integer key : set) {
                        answer[i][j] += moveCount.get(key); 
                    }
                }
                sb.append((answer[i][j]) % 10);
            }
            sb.append("\n");
        }   

        sb.deleteCharAt(sb.length()-1);
        System.out.println(sb);
    }
}

// 스타트 택시

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_19238 {
    static int N;
    static int fuel; // 연료
    static int[][] map;
    static int[][] visited;
    static int[][] direction = new int[][] {{-1, 0}, {1, 0}, {0, 1}, {0, -1}};

    static int[] findPassenger(int[] now, int count) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(now);
        visited[now[0]][now[1]] = count;
        int nextX; 
        int nextY;
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> {
            if (o1[0] != o2[0]) return o1[0] - o2[0];
            return o1[1] - o2[1];
        });
        
        int spendFuel = 0;
        while (!queue.isEmpty()) {
            Queue<int[]> nextQueue = new LinkedList<>();
            while (!queue.isEmpty()) {
                now = queue.poll();
                
                if (map[now[0]][now[1]] > 1) {
                    pq.add(new int[] {now[0], now[1], map[now[0]][now[1]], spendFuel});
                }

                for (int i = 0; i < 4; i++) {
                    nextX = now[0] + direction[i][0];        
                    nextY = now[1] + direction[i][1];
                    
                    if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= N || map[nextX][nextY] == 1 || visited[nextX][nextY] == count) continue;

                    nextQueue.add(new int[] {nextX, nextY});
                    visited[nextX][nextY] = count;
                }
            }
            spendFuel++;
            if (!pq.isEmpty()) {
                return pq.poll();
            }

            queue = nextQueue;
        }

        return new int[] {-1, -1, -1};
    }

    static int[] findDestination(int[] now, int[] destinationPos, int count) {
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[] {now[0], now[1], 0});
        int nextX; 
        int nextY;
        while (!queue.isEmpty()) {
            now = queue.poll();
            
            for (int i = 0; i < 4; i++) {
                nextX = now[0] + direction[i][0];        
                nextY = now[1] + direction[i][1];
                
                if (nextX < 0 || nextX >= N || nextY < 0 || nextY >= N || map[nextX][nextY] == 1 || visited[nextX][nextY] == count) continue;
                
                if (nextX == destinationPos[0] && nextY == destinationPos[1]) {
                    return new int[] {nextX, nextY, now[2]+1};
                }
                queue.add(new int[] {nextX, nextY, now[2]+1});
                visited[nextX][nextY] = count;
            }
        }
  
        return new int[] {-1, -1, -1};
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        fuel = Integer.parseInt(st.nextToken());

        // 지도 입력 
        map = new int[N][N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        // 출발지 목적지
        st = new StringTokenizer(br.readLine());
        int startX = Integer.parseInt(st.nextToken());
        int startY = Integer.parseInt(st.nextToken());
        
        // 승객의 출발지와 목적지
        int passX; int passY; int destX; int destY;
        int[][] destinationList = new int[M+2][2];
        for (int i = 2; i <= M+1; i++) {
            st = new StringTokenizer(br.readLine());
            passX = Integer.parseInt(st.nextToken());
            passY = Integer.parseInt(st.nextToken());
            destX = Integer.parseInt(st.nextToken());
            destY = Integer.parseInt(st.nextToken());
            map[passX-1][passY-1] = i;
            destinationList[i] = new int[] {destX-1, destY-1};
        }

        visited = new int[N][N];
        int count = 1;
        int[] passengerPos;
        int[] destinationPos = new int[] {startX-1, startY-1};
        while (true) {
            
            passengerPos = findPassenger(new int[] {destinationPos[0], destinationPos[1]}, count);
            if ((passengerPos[0] == -1 && passengerPos[1] == -1) || (fuel < passengerPos[3])) {
                fuel = -1;
                break;
            }

            fuel -= passengerPos[3];
            map[passengerPos[0]][passengerPos[1]] = 0;
            count++;

            destinationPos = findDestination(new int[] {passengerPos[0], passengerPos[1]}, destinationList[passengerPos[2]], count);
            if ((destinationPos[0] == -1 && destinationPos[1] == -1) || (fuel < destinationPos[2])) {
                fuel = -1;
                break;
            }

            fuel += destinationPos[2];
            count++;

            M--;
            if (M == 0) {
                break;
            }
        }

        System.out.println(fuel);
    }
}

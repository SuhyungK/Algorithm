// ㅂ

// 비밀번호 제작

package Baekjoon.Platinum;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class baekjoon_20304 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int M = Integer.parseInt(br.readLine());
        int[] visited = new int[N+1];

        Queue<Integer> queue = new LinkedList<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            int x = Integer.parseInt(st.nextToken());
            queue.add(x);
            visited[x] = 0;
        }
        
        int maxHighSafety = 0;
        int maxBinbaryLength = Integer.toBinaryString(N).length();
        
        while (!queue.isEmpty()) {
            int x = queue.poll();
            
            for (int i = 0; i < maxBinbaryLength; i++) {
                int nextX = x ^ (1 << i);
                if (nextX > N || visited[nextX] != 0) continue;
                visited[nextX] = visited[x] + 1;
                queue.add(nextX);
                maxHighSafety = Math.max(maxHighSafety, visited[nextX]);
            }

        }
        System.out.println(maxHighSafety);
    }
}


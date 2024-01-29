// ACM Craft

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_1005 {
    static BufferedReader br;
    static int solution() throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] builtTime = new int[N+1];
        int[] connectCount = new int[N+1];
        List<List<Integer>> builtOrder = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            builtOrder.add(new ArrayList<>());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            builtTime[i] = Integer.parseInt(st.nextToken());
        }
        
        int X;
        int Y;
        for (int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            X = Integer.parseInt(st.nextToken());
            Y = Integer.parseInt(st.nextToken());
            connectCount[Y]++;
            builtOrder.get(X).add(Y);
        }

        int W = Integer.parseInt(br.readLine());
        
        Queue<Integer> queue = new LinkedList<>();
        for (int i = 1; i <= N; i++) {
            if (connectCount[i] == 0) {
                queue.add(i);
            }
        }

        int[] answer = Arrays.copyOf(builtTime, N+1);
        while (!queue.isEmpty()) {
            Queue<Integer> nextQueue = new LinkedList<>();
            while (!queue.isEmpty()) {
                int w = queue.poll();
                int timeW = answer[w];

                for (int nextW : builtOrder.get(w)) {
                    connectCount[nextW]--;
                    answer[nextW] = Math.max(answer[nextW], builtTime[nextW] + timeW);
                    if (connectCount[nextW] == 0) {
                        nextQueue.add(nextW);
                    }
                }
            }
            queue = nextQueue;
        }
        return answer[W];
    }
    public static void main(String[] args) throws IOException {
        br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < T; i++) {
            sb.append(solution() + "\n");
        }
        sb.replace(sb.length()-1, sb.length(), "");
        System.out.println(sb);
    }
}

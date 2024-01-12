// 특정한 최단 경로 

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_1504 {
    static int N;
    static int E;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        E = Integer.parseInt(st.nextToken());

        List<List<long[]>> graph = new ArrayList<>();
        for (int i = 0; i < N+1; i++) {
            graph.add(new ArrayList<>());
        }

        for (int i = 0; i < E; i++) {
            st = new StringTokenizer(br.readLine());
            int v1 = Integer.parseInt(st.nextToken());
            int v2 = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.get(v1).add(new long[]{v2, c});
            graph.get(v2).add(new long[]{v1, c});
        }

        st = new StringTokenizer(br.readLine());
        int u = Integer.parseInt(st.nextToken());
        int v = Integer.parseInt(st.nextToken());
        long[] uDistance = shortDistance(u, graph);
        long[] vDistance = shortDistance(v, graph);


        System.out.println(solution(uDistance, vDistance, u, v));
    }

    private static long solution(long[] distance1, long[] distance2, int u, int v) {
        if (E == 0 || distance1[1] == Long.MAX_VALUE || distance1[u] == Long.MAX_VALUE || distance1[N] == Long.MAX_VALUE ||
                distance2[1] == Long.MAX_VALUE || distance2[N] == Long.MAX_VALUE) return -1;

        return Math.min(distance1[1] + distance1[v] + distance2[N], distance2[1] + distance2[u] + distance1[N]);
    }

    /**
     * 특정 정점에 대해 다른 모든 정점에 대한 최단 거리 구하기
     */
    private static long[] shortDistance(int start, List<List<long[]>> graph) {
        PriorityQueue<long[]> pQ = new PriorityQueue<>(Comparator.comparingLong(arr -> arr[1]));
        long[] distance = new long[N+1];
        Arrays.fill(distance, Long.MAX_VALUE);
        distance[start] = 0;
        pQ.add(new long[]{start, 0});

        while (!pQ.isEmpty()) {
            long[] now = pQ.poll();

            int nowNode = (int) now[0];
            if (now[1] > distance[nowNode]) continue;
            for (long[] next : graph.get(nowNode)) {
                int nextNode = (int) next[0];
                long addDistance = next[1];
                if (distance[nextNode] > now[1] + addDistance) {
                    distance[nextNode] = now[1] + addDistance;
                    pQ.add(new long[]{nextNode, distance[nextNode]});
                }
            }
        }

        return distance;
    }
}
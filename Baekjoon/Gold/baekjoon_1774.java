// 우주신과의 교감

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class baekjoon_1774 {
    static int[] parent;
    static int find(int x) {
        if (parent[x] != x) {
            return parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x <= y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int[][] spaces = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            spaces[i][0] = Integer.parseInt(st.nextToken());
            spaces[i][1] = Integer.parseInt(st.nextToken());
        }

        parent = new int[N];
        for (int i = 0; i < N; i++) {
            parent[i] = i;
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int s1 = Integer.parseInt(st.nextToken())-1;
            int s2 = Integer.parseInt(st.nextToken())-1;

            if (find(s1) != find(s2)) {
                union(s1, s2);
            }
        }

        PriorityQueue<SpaceDistance> pq = new PriorityQueue<>();
        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                pq.add(new SpaceDistance(i, j, cal(spaces[i], spaces[j])));
            }
        }

        double cost = 0.0;
        while (!pq.isEmpty()) {
            SpaceDistance sd = pq.poll();
            if (find(sd.s1) != find(sd.s2)) {
                cost += sd.dist;
                union(sd.s1, sd.s2);
            }
        }

//        cost = Math.round((cost*100) / 100.0);
        System.out.printf(String.format("%.2f", cost));
    }

    static class SpaceDistance implements Comparable<SpaceDistance>{
        int s1;
        int s2;
        double dist;

        public SpaceDistance(int s1, int s2, double dist) {
            this.s1 = s1;
            this.s2 = s2;
            this.dist = dist;
        }

        @Override
        public int compareTo(SpaceDistance o) {
            return Double.compare(this.dist, o.dist);
        }
    }

    private static double cal(int[] s1, int[] s2) {
        return Math.sqrt(Math.pow((s1[0] - s2[0]), 2) + Math.pow((s1[1] - s2[1]), 2));
    }
}
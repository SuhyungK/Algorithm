// 전기가 필요해

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class baekjoon_10423 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        boolean[] MST = new boolean[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < K; i++) {
            MST[Integer.parseInt(st.nextToken())-1] = true;
        }

        List<List<Cable>> infos = new ArrayList<>();
        for (int i = 0; i < N; i++) {
            infos.add(new ArrayList<>());
        }

        PriorityQueue<Cable> pq = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken())-1;
            int v = Integer.parseInt(st.nextToken())-1;
            int w = Integer.parseInt(st.nextToken());

            infos.get(u).add(new Cable(u, v, w));
            infos.get(v).add(new Cable(v, u, w));
            if (MST[u] || MST[v]) {
                // 둘 중 하나라도 발전소인 경우
                pq.add(new Cable(u, v, w));
            }
        }

        Long cost = 0L;
        while (!pq.isEmpty()) {
            Cable c = pq.poll();

            if (MST[c.u] && MST[c.v]) continue;
            cost += c.w;
            if (MST[c.u]) {
                pq.addAll(infos.get(c.v));
                MST[c.v] = true;
            } else {
                pq.addAll(infos.get(c.u));
                MST[c.u] = true;
            }
        }

        System.out.println(cost);
    }

    static class Cable implements Comparable<Cable> {
        int u;
        int v;
        int w;

        public Cable(int u, int v, int w) {
            this.u = u;
            this.v = v;
            this.w = w;
        }

        @Override
        public int compareTo(Cable o) {
            return this.w - o.w;
        }
    }

}
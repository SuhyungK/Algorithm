// 전력난

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_6497 {
    static int[] parent;

    static int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
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
        while (true) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int m = Integer.parseInt(st.nextToken());
            int n = Integer.parseInt(st.nextToken());
            
            if (m == 0 && n == 0) {
                System.exit(0);
            }
            PriorityQueue<Road> pq = new PriorityQueue<>();
            int x; int y; int z;
            long cost = 0;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                z = Integer.parseInt(st.nextToken());
                cost += z;
                pq.add(new Road(x, y, z));
            }
            
            parent = new int[m];
            for (int i = 0; i < m; i++) {
                parent[i] = i;
            }

            while (!pq.isEmpty()) {
                Road cur = pq.poll();
                
                if (find(cur.x) != find(cur.y)) {
                    union(cur.x, cur.y);
                    cost -= cur.z;
                }
            }

            System.out.println(cost);
        }
    }
}

class Road implements Comparable<Road> {
    int x;
    int y;
    int z;

    Road(int x, int y, int z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    @Override
    public int compareTo(Road o) {
        return this.z - o.z;
    }
}
import java.util.*;
import java.io.*;

public class baekjoon_2887 {
    static int[] parent;
    static int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x < y) {
            parent[y] = x;
        } else {
            parent[x] = y;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][4];
        StringTokenizer st;
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            arr[i][0] = i;
            arr[i][1] = Integer.parseInt(st.nextToken());
            arr[i][2] = Integer.parseInt(st.nextToken());
            arr[i][3] = Integer.parseInt(st.nextToken());
        }

        long[][] edges = new long[3*(N-1)][3];
        int idx;
        for (int i = 1; i <= 3; i++) {
            final int index = i;
            Arrays.sort(arr, Comparator.comparingInt(o -> o[index]));
            
            for (int j = 0; j < N-1; j++) {
                idx = (N-1)*(i-1) + j;
                edges[idx][0] = arr[j+1][i] - arr[j][i];
                edges[idx][1] = arr[j][0];
                edges[idx][2] = arr[j+1][0];
            }
        }
        
        Arrays.sort(edges, Comparator.comparingLong(o -> o[0]));
        parent = new int[N];

        for (int i = 0; i < N; i++) {
            parent[i] = i;    
        }

        int x;
        int y;
        long answer = 0;
        for (int i = 0; i < edges.length; i++) {
            x = (int) edges[i][1];
            y = (int) edges[i][2];
            if (find(x) == find(y)) continue;
            union(x, y);
            answer += edges[i][0];
        }
        System.out.println(answer);
    }
}
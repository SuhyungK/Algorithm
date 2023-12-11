// 회사 문화 1

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_14267 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        
        int n = Integer.parseInt(st.nextToken());
        int m  = Integer.parseInt(st.nextToken());
        int[] parent = new int[n+1]; // 부모 노드
        int[] degree = new int[n+1]; // 칭찬의 정도
        
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i < n+1; i++) {
            parent[i] = Integer.parseInt(st.nextToken());    
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            degree[p] += w;
        }
        
        int par;
        for (int i = 2; i < n+1; i++) {
            par = parent[i];
            degree[i] += degree[par];
        }

        StringBuilder sb = new StringBuilder();

        for (int i = 1; i < n+1; i++) {
            sb.append(degree[i]).append(" ");
        }
        System.out.println(sb);
    }
}

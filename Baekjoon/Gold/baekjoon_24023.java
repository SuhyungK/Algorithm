package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_24023 {
    static int N;
    static int K;
    static int[] A;

    static int[] sol() {
        int s = 0;
        int e = 0;

        int sum = 0;
        for (int i = 0; i < N; i++) {
            sum |= A[i];
            if ((sum | K) != K) {
                sum = 0;
                s = i+1;
                e = s;
            } else {
                if (sum == K) {
                    return new int[] {s+1, e+1};
                }
                e++;
            }
        }
        return new int[] {-1};
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        A = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }

         int[] answer = sol();
         StringBuilder sb = new StringBuilder();
         for (int x : answer) {
             sb.append(x + " ");
         }
         sb.deleteCharAt(sb.length() - 1);
         System.out.println(sb);
    }
}
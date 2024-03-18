// 생일 선물

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_12892 {
    static final int MOD = 1_000_000_007;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        
        int P;
        int V;
        int[][] gifts = new int[N][2];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            P = Integer.parseInt(st.nextToken());
            V = Integer.parseInt(st.nextToken());
            gifts[i][0] = P;
            gifts[i][1] = V;
        }

        Arrays.sort(gifts, (o1, o2) -> o1[0] - o2[0]);
        
        int low = 0;
        long maxSum = 0;
        long tmpSum = 0;
        for (int i = 0; i < N; i++) {
            tmpSum += gifts[i][1];
            while (gifts[i][0] >= gifts[low][0] + D) {
                tmpSum -= gifts[low][1];
                low++;
            }
            maxSum = Math.max(maxSum, tmpSum);
        }

        System.out.println(maxSum);
    }
}
// 택배

package Baekjoon.Gold;

import java.io.*;
import java.util.*;

public class baekjoon_8980 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int C = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(br.readLine());

        int[][] boxInfo = new int[M][3];
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            boxInfo[i][0] = Integer.parseInt(st.nextToken());
            boxInfo[i][1] = Integer.parseInt(st.nextToken());
            boxInfo[i][2] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(boxInfo, (a, b) -> {
            return (a[1]) - (b[1]);
        });

        long[] road = new long[N];
        long totalCnt = 0;
        for (int[] box : boxInfo) {
            int from = box[0];
            int to = box[1];
            int count = box[2];

            long maxCnt = 0;
            for (int i = from; i < to; i++) {
                maxCnt = Math.max(maxCnt, road[i]);
            }
            
            long add = Math.min(count, C - maxCnt);
            for (int i = from; i < to; i++) {
                road[i] += add;
            }
            totalCnt += add;
        }
        System.out.println(totalCnt);
    }
}
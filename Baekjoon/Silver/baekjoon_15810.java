package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_15810 {
    static int[] staffTimes;
    static int N, M;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        staffTimes = new int[N];
        st = new StringTokenizer(br.readLine());
        int minValue = Integer.MAX_VALUE;
        for (int i = 0; i < staffTimes.length; i++) {
            staffTimes[i] = Integer.parseInt(st.nextToken());
            minValue = Math.min(minValue, staffTimes[i]);
        }

        long left = 0;
        long right = minValue * M;
        long mid = 0;
        while (left+1 < right) {
            mid = (left + right) / 2;
            long count = 0;
            for (int i = 0; i < staffTimes.length; i++) {
                count += (mid / staffTimes[i]);
            }

            if (count >= M) {
                right = mid;
            } else {
                left = mid;
            }
        }
        
        System.out.println(right);
    }
}

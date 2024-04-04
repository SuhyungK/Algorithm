// 입국심사

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_3079 {
    static int N;
    static int M;
    static int[] time;
    static final int MAX_TIME = 1_000_000_000;
    static final int MAX_M = 1_000_000_000;

    static boolean pass(long midTime) {
        long m = 0;
        for (int t : time) {
            m += midTime / t;
            if (m >= M) break;
        }

        return m >= M;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        time = new int[N];
        for (int i = 0; i < N; i++) {
            time[i] = Integer.parseInt(br.readLine());
        }

        long maxTime = (long) MAX_TIME * MAX_M;
        long minTime = 1;
        long midTime;
        while (minTime <= maxTime) {
            midTime = (minTime + maxTime) / 2;

            if (pass(midTime)) {
                maxTime = midTime - 1;
            } else {
                minTime = midTime + 1;
            }
        }

        System.out.println(minTime);
    }
}
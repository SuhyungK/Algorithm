// 주유소

package Baekjoon.Silver;

import java.io.*;
import java.util.*;

public class baekjoon_13305 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        long[] DISTANCE = new long[N-1];
        for (int i = 0; i < N-1; i++) {
            DISTANCE[i] = Long.parseLong(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        long[] LITER = new long[N];
        for (int i = 0; i < N; i++) {
            LITER[i] = Long.parseLong(st.nextToken());
        }

        long cost = 0;
        for (int i = 0; i < N-1; i++) {
            cost += LITER[i] * DISTANCE[i];
            if (LITER[i+1] > LITER[i]) {
                LITER[i+1] = LITER[i];
            }
        }

        System.out.println(cost);
    }
}

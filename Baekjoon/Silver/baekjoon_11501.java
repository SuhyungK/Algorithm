// 주식

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_11501 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());
        StringTokenizer st;
        for (int i = 0; i < T; i++) {
            int N = Integer.parseInt(br.readLine());
            int[] stock = new int[N];
            st = new StringTokenizer(br.readLine());
            for (int j = N-1; j > -1; j--) {
                stock[j] = Integer.parseInt(st.nextToken()); 
            }

            long totalProfit = 0;
            int maxStock = Integer.MIN_VALUE;
            for (int j = 0; j < N; j++) {
                if (stock[j] > maxStock) {
                    maxStock = stock[j];
                } else {
                    totalProfit += maxStock - stock[j];
                }
            }
            System.out.println(totalProfit);
        }
    }
}

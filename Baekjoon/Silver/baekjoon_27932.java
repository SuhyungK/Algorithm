// 어깨동무

package Baekjoon.Silver;

import java.util.*;
import java.io.*;


public class baekjoon_27932 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] height = new int[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            height[i] = Integer.parseInt(st.nextToken());
        }

        int low = 0;
        int high = 1_000_000_000;
        int H;
        boolean flag;
        while (low <= high) {
            H = (low + high) / 2;

            flag = false;
            int count = 0;
            for (int i = 1; i < n; i++) {

                if (Math.abs(height[i] - height[i-1]) <= H) {
                    flag = false;
                    continue;
                }

                if (!flag) {
                    count++;
                    flag = true;
                } 
                count++;
            }

            System.out.println(low + " " + H + " " + high + " " + count);

            if (count > k) {
                low = H + 1;
            } else {
                high = H - 1;
            }
        }

        System.out.println(low);
    }
}
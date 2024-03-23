// 아 저는 볶음밥이요

package Baekjoon.Silver;

import java.util.*;
import java.io.*;

public class baekjoon_23814 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long D = sc.nextLong();

        long n = sc.nextLong() % D;
        long m = sc.nextLong() % D;
        long K = sc.nextLong();


        long ans = 0;
        long maxTmp = 0;

        long tmpK = K - (D - n) - (D - m);
        if (tmpK / D + 2 >= maxTmp) {
            maxTmp = tmpK / D + 2;
            ans = tmpK;
        }

        tmpK = Math.max(K - (D - m), K - (D - n));
        if (tmpK / D + 1 >= maxTmp) {
            maxTmp = tmpK / D + 1;
            ans = tmpK;
        }

        if (K / D >= maxTmp) {
            ans = K;
        }

        System.out.println(ans);
    }
}
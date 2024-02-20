// 용돈 관리 

package Baekjoon.Silver;

import java.io.IOException;
import java.util.Scanner;

public class baekjoon_6236 {
        static final long MAX_N = 100_000;
    static final long MAX_DAY_CASH = 10_000;

    static int N;
    static int M;
    static long[] passbook;

    static boolean run(long K) {
        int count = 1;
        long leftMoney = K;
        for (long cash : passbook) {

            if (cash > K) {
                return false;
            }

            if (cash <= leftMoney) {
                leftMoney -= cash;
            } else {
                leftMoney = K - cash;
                count++;
            }
        }
        return count <= M;
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        M = sc.nextInt();

        passbook = new long[N];
        for (int i = 0; i < N; i++) {
            passbook[i] = sc.nextLong();
        }

        long low = 0;
        long high = MAX_N * MAX_DAY_CASH;
        while (low <= high) {
            long k = (low + high) / 2;
            
            boolean result = run(k);
            // System.out.println("===" + low + " " + k + " " + high + " " + result + "===");

            if (result) {
                high = k - 1;
            } else {
                low = k + 1;
            }
        }

        System.out.println(low);
    }
}

// 홀수 홀릭 호석

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class baekjoon_20164 {
        static long maxCount;
    static long minCount = Long.MAX_VALUE;
    static String N;

    static void calc(String n, long oddCount) {
        oddCount += countOdd(n);
        if (n.length() == 1) {
            maxCount = Math.max(maxCount, oddCount);
            minCount = Math.min(minCount, oddCount);
            return;
        }

        if (n.length() == 2) {
            int tmp = Integer.parseInt(String.valueOf(n.charAt(0))) + Integer.parseInt(String.valueOf(n.charAt(1)));
            calc(String.valueOf(tmp), oddCount);
            return;
        }

        for (int i = 0; i < n.length() - 2; i++) {
            int front = getSum(n, 0, i);
            for (int j = i + 1; j < n.length()- 1; j++) {
                int middle = getSum(n, i + 1, j);
                int back = getSum(n, j + 1, n.length() - 1);
                int tmp = front + middle + back;
                String next = String.valueOf(tmp);
                calc(next, oddCount);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        N = sc.next();

        /**
         * 1. 수에서 홀수의 개수 세기
         * 2. 수의 자릿수에 따른 연산
         * 2-1. 한 자리면 종료
         * 2-2. 두 자리면 2개로 나눠서 합하고 새로운 수 생성
         * 2-3. 세 자리 이상이면 "임의의 위치"에서 3개의 수로 분할(임의의 위치는 2군데) 3개를 더한 값을 새로운 수로 생각
         */
        calc(N, 0);
        System.out.println(minCount + " " + maxCount);
    }

    private static long countOdd(String n) {
        return Arrays.stream(n.split(""))
                     .mapToInt(Integer::parseInt)
                     .filter(i -> i % 2 == 1)
                     .count();
    }

    private static int getSum(String n, int startIdx, int endIdx) {
        return Integer.parseInt(n.substring(startIdx, endIdx+1));
    }
}

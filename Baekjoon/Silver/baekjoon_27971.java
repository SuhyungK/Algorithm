// 강아지는 많을수록 좋다

package Silver;

import java.io.IOException;
import java.util.Arrays;
import java.util.Scanner;

public class baekjoon_27971 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int A = sc.nextInt();
        int B = sc.nextInt();

        int[] arr = new int[N+1];
        int l; int r;
        for (int i = 0; i < M; i++) {
            l = sc.nextInt();
            r = sc.nextInt();
            arr[l] -= 1;
            arr[r + 1] += 1;
        }

        for (int i = 1; i < N + 1; i++) {
            arr[i] += arr[i - 1];
        }

        int[] dp = new int[N + 1];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;
        for (int i = 0; i < N + 1; i++) {
            if (arr[i] < 0 || dp[i] == Integer.MAX_VALUE) {
                continue;
            }

            if (i + A <= N) {
                dp[i + A] = Math.min(dp[i + A], dp[i] + 1);
            }

            if (i + B <= N) {
                dp[i + B] = Math.min(dp[i + B], dp[i] + 1);
            }
        }

        if (dp[N] == Integer.MAX_VALUE) {
            System.out.println(-1);
        }
        else {
            System.out.println(dp[N]);
        }
    }
}

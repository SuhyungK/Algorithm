package PGM.Lv3.스티커모으기;

public class Solution {
    static int n;
    public int solution(int sticker[]) {
        // 맨 앞 숫자 포함 O -> 맨 마지막 포함 X
        // 맨 앞 숫자 포함 X -> 맨 마지막 포함 O, X

        n = sticker.length;
        if (n == 1) {
            return sticker[0];
        } else if (n == 2) {
            return Math.max(sticker[0], sticker[1]);
        }

        int answer;

        // 1. 맨 앞을 반드시 포함하는 경우
        int[][] dp1 = new int[n][2];
        dp1[0][0] = sticker[0];
        dp1[1][1] = sticker[0];

        // 2. 맨 앞을 포함하지 않는 경우
        int[][] dp2 = new int[n][2];
        dp2[1][0] = sticker[1];
        return Math.max(getMaxSum(sticker, dp1, n-1), getMaxSum(sticker, dp2, n));

    }

    int getMaxSum(int[] sticker, int[][] dp, int end) {
        for (int i = 2; i < end; i++) {
            dp[i][0] = Math.max(dp[i-2][0], dp[i-2][1]) + sticker[i];
            dp[i][1] = Math.max(dp[i-1][0], dp[i-1][1]);
        }
        return Math.max(dp[end-1][0], dp[end-1][1]);
    }
}

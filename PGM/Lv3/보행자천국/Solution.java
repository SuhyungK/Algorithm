package PGM.Lv3.보행자천국;

public class Solution {
    int MOD = 20170805;
    public int solution(int m, int n, int[][] cityMap) {
        int[][][] dp = new int[m][n][2];
        int[] dx = new int[] {-1, 0};
        int[] dy = new int[] {0, -1};

        dp[0][0][0] = 1;
        dp[0][0][1] = 1;
        for (int i = 1; i < m; i++) {
            if (cityMap[i][0] == 0) {
                dp[i][0][0] = dp[i-1][0][0];
                dp[i][0][1] = dp[i-1][0][0];
            } else if (cityMap[i][0] == 2) {
                dp[i][0][0] = dp[i-1][0][0];
            }
        }

        for (int j = 1; j < n; j++) {
            if (cityMap[0][j] == 0) {
                dp[0][j][0] = dp[0][j-1][1];
                dp[0][j][1] = dp[0][j-1][1];
            } else if (cityMap[0][j] == 2) {
                dp[0][j][1] = dp[0][j-1][1];
            }
        }


        for (int i = 1; i < m; i++) {
            for (int j = 1; j < n; j++) {
                if (cityMap[i][j] == 0) {
                    dp[i][j][0] = (dp[i-1][j][0] + dp[i][j-1][1]) % MOD;
                    dp[i][j][1] = (dp[i-1][j][0] + dp[i][j-1][1]) % MOD;
                } else if (cityMap[i][j] == 2) {
                    dp[i][j][0] = dp[i-1][j][0];
                    dp[i][j][1] = dp[i][j-1][1];
                }
            }
        }

        return Math.max(dp[m-1][n-1][0], dp[m-1][n-1][1]) % MOD;
    }
}
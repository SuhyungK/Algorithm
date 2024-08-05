package PGM.Lv2.양궁대회;

import java.util.*;

public class Solution {
    static int[] answer = new int[] {-1};
    static int gap = 0;
    static int[] apeachInfo;
    public int[] solution(int n, int[] info) {
        apeachInfo = info;

        int apeachScore = 0;
        for (int i = 0; i < 10; i++) {
            if (apeachInfo[i] > 0) {
                apeachScore += 10 - i;
            }
        }
        shoot(9, n, new int[11], 0, apeachScore);
        return answer;
    }

    public void shoot(int i, int n, int[] ryanInfo, int ryanScore, int apeachScore) {
        if (i == -1 || n == 0) {
            // 더 이상 쏠 수 없음
            if (ryanScore - apeachScore > gap) {
                gap = ryanScore - apeachScore;
                // System.out.println(ryanScore + " " + apeachScore + " " + Arrays.toString(ryanInfo));
                ryanInfo[10] = n;
                answer = Arrays.copyOf(ryanInfo, ryanInfo.length);
                ryanInfo[10] = 0;
            }
            return;
        }

        if (apeachInfo[i] < n) {
            ryanInfo[i] = apeachInfo[i] + 1;
            shoot(i - 1, n - apeachInfo[i] - 1, ryanInfo, ryanScore + (10 - i), apeachInfo[i] > 0 ? apeachScore - (10 - i) : apeachScore);
            ryanInfo[i] = 0;
        }
        shoot(i - 1, n, ryanInfo, ryanScore, apeachScore);
    }
}

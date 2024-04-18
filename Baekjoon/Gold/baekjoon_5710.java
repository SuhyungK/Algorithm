// 전기 요금

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_5710 {
    static int N;
    static int[][] steps = new int[][] {{100, 2}, {9900, 3}, {990000, 5}};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();
        while (true) {
            st = new StringTokenizer(br.readLine());
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());

            if (A == 0 && B == 0) break;

            int sumUsage = feeToUsage(A);
            int maxUsage = sumUsage;
            int minUsage = 0;
            while (minUsage <= maxUsage) {
                int xUsage = (maxUsage + minUsage) / 2;

                int diff = Math.abs(usageToFee(sumUsage - xUsage) - usageToFee(xUsage));
                if (diff == B) {
                    sb.append(usageToFee(Math.min((sumUsage - xUsage), xUsage)) + "\n");
                    break;
                } else if (diff > B) {
                    minUsage = xUsage;
                } else {
                    maxUsage = xUsage;
                }
            }
        }
        sb.deleteCharAt(sb.length()-1);
        System.out.println(sb);
    }

    private static int feeToUsage(int fee) {
        int usage = 0;
        for (int[] step : steps) {
            if (fee > step[0] * step[1]) {
                usage += step[0];
                fee -= step[0] * step[1];
            } else {
                usage += fee / step[1];
                fee = 0;
                break;
            }
        }
        return usage + fee / 7;
    }

    private static int usageToFee(int usage) {
        int fee = 0;
        for (int[] step : steps) {
            if (usage > step[0]) {
                fee += step[0] * step[1];
                usage -= step[0];
            } else {
                fee += usage * step[1];
                usage = 0;
                break;
            }
        }
        return fee + usage * 7;
    }

}
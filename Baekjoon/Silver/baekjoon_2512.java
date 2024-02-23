// 예산

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_2512 {
        static boolean binarySearch(int[] budgets, int target, int M) {
        int needBudget = 0;
        for (int i = 0; i < budgets.length; i++) {
            needBudget += Math.min(budgets[i], target);

            if (needBudget > M) {
                // System.out.println(needBudget);
                return false;
            }
        }

        return needBudget <= M;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        int[] budgets = new int[N];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            budgets[i] = Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        
        int highBudget = 1_000_000_000;
        int lowBudget = 1;
        while (lowBudget <= highBudget) {
            int mid = (lowBudget + highBudget) / 2;

            if (binarySearch(budgets, mid, M)) {
                lowBudget = mid + 1;
            } else {
                highBudget = mid - 1;
            }
        }

        int maxBudget = 0;
        for (int i = 0; i < budgets.length; i++) {
            maxBudget = Math.max(maxBudget, Math.min(highBudget, budgets[i]));
        }
        System.out.println(maxBudget);
    }
}

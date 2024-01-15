import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st;
        for (int t = 1; t < 11; t++) {
            int N = Integer.parseInt(br.readLine());

            int[][] arr = new int[100][100];
            for (int i = 0; i < 100; i++) {
                st = new StringTokenizer(br.readLine());
                for (int j = 0; j < arr.length; j++) {
                    arr[i][j] = Integer.parseInt(st.nextToken());
                } 
            }

            int maxSum = Integer.MIN_VALUE;

            // 행 계산
            for (int i = 0; i < 100; i++) {
                int rowSum = 0;
                for (int j = 0; j < 100; j++) {
                    rowSum += arr[i][j];
                }
                maxSum = Math.max(maxSum, rowSum);
            }

            // 열 계산
            for (int j = 0; j < 100; j++) {
                int colSum = 0;
                for (int i = 0; i < 100; i++) {
                    colSum += arr[i][j];
                }
                maxSum = Math.max(maxSum, colSum);
            }

            // 왼쪽 -> 아래 대각선
            int dagSum1 = 0;
            for (int i = 0; i < 100; i++) {
                dagSum1 += arr[i][i];
            }
            maxSum = Math.max(maxSum, dagSum1);
            
            int dagSum2 = 0;
            for (int i = 0; i < 100; i++) {
                dagSum2 += arr[i][100 - i - 1];
            }
            maxSum = Math.max(maxSum, dagSum2);

            System.out.println("#" + t + " " + maxSum);
        }
    }
}

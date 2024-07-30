package PGM.Lv3.연속펄스부분수열의합;

public class Solution {
    static int n;
    public long solution(int[] sequence) {
        n = sequence.length;

        return Math.max(getMaxSum(getArr(1, sequence)), getMaxSum(getArr(-1, sequence)));
    }

    long[] getArr(int u, int[] arr) {
        long[] temp = new long[n];
        temp[0] = arr[0] * u;
        for (int i = 1; i < n; i++) {
            u *= -1;
            temp[i] = arr[i] * u + temp[i-1];
        }
        return temp;
    }

    long getMaxSum(long[] arr) {
        long minValue = 0;
        long maxSum = Long.MIN_VALUE;

        for (int i = 0; i < n; i++) {
            maxSum = Math.max(maxSum, arr[i] - minValue);
            if (arr[i] < minValue) {
                minValue = arr[i];
            }
        }
        return maxSum;
    }
}

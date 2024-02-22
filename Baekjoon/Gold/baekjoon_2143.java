// 두 배열의 합

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class baekjoon_2143 {
        static void findSumOfSubarray(long[] arr, Map<Long, Long> map) {
        for (int i = 1; i < arr.length; i++) {
            for (int j = 0; j < i; j++) {
                map.put(arr[i] - arr[j], map.getOrDefault(arr[i] - arr[j], 0L) + 1L);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        int n = Integer.parseInt(br.readLine());
        long[] A = new long[n+1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= n; i++) {
            A[i] = Long.parseLong(st.nextToken());
            A[i] += A[i-1];
        }

        int m = Integer.parseInt(br.readLine());
        long[] B = new long[m+1];
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= m; i++) {
            B[i] = Long.parseLong(st.nextToken());
            B[i] += B[i-1];
        }

        long answer = 0;
        Map<Long, Long> mapA = new HashMap<>();
        Map<Long, Long> mapB = new HashMap<>();
        findSumOfSubarray(A, mapA);
        findSumOfSubarray(B, mapB);
        for (Long key : mapA.keySet()) {
            answer += mapA.get(key) * mapB.getOrDefault(T - key, 0L);
        }
        System.out.println(answer);
    }
}

// 부분 수열의 합 2

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class baekjoon_1208 {
    static Map<Long, Long> getSubsetSum(long[] sequence, long S) {
        int n = sequence.length;
        Map<Long, Long> subsetSum = new HashMap<>();
        for (int i = 0; i < Math.pow(2, n); i++) {
            long tmpSum = 0;
            for (int j = 0; j < n; j++) {
                if ((i & (1 << j)) != 0) {
                    tmpSum += sequence[j];
                }
            }
            
            subsetSum.put(tmpSum, subsetSum.getOrDefault(tmpSum, 0L) + 1);
        }
        return subsetSum;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        long S = Long.parseLong(st.nextToken());

        long[] sequence = new long[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            sequence[i] = Long.parseLong(st.nextToken());
        }

        Map<Long, Long> A = getSubsetSum(Arrays.copyOfRange(sequence, 0, N / 2), S);
        Map<Long, Long> B = getSubsetSum(Arrays.copyOfRange(sequence, N / 2, N), S);

        long answer = 0;
        System.out.println(A);
        System.out.println(B);
        for (Long sum : A.keySet()) {
            answer += (A.get(sum) * B.getOrDefault(S - sum, 0L));
        }

        if (S == 0) answer--;
        System.out.println(answer);
    }
}

// 수열

package Silver;

import java.util.Scanner;

public class baekjoon_2559 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();

        int[] arr = new int[N];
        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }
        
        sc.close();

        int sum = 0;
        for (int i = 0; i < K; i++) {
            sum += arr[i];
        }
        System.out.println("sum = " + sum);
        

        int startIdx = 0;
        int tmpSum = sum;
        while (startIdx < (N - K)) {

            tmpSum = tmpSum - arr[startIdx] + arr[startIdx+K];
            sum = Math.max(sum, tmpSum);
            System.out.println("tmpSum = " + tmpSum);
            startIdx++;
        }

        System.out.println(sum);
    }
}

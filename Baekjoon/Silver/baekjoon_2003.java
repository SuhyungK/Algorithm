// 수들의 합 2

package Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class baekjoon_2003 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine(), " ");
        int[] arr = new int[N];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int p1 = 0; int p2 = 0;
        int sum = 0;
        int answer = 0;

        while (!(sum < M && p2 >= N)) {
            if (sum == M) answer++;
            
            if (sum >= M) {
                sum -= arr[p1];
                p1++;
            } else {
                sum += arr[p2];
                p2++;
            }
        }
        System.out.println(answer);
    }
}

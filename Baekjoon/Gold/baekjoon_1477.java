// 휴게소 세우기

package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class baekjoon_1477 {
        static int[] restStop;
    
    static int run(int mid) {
        int count = 0;
        for (int i = 1; i <= restStop.length-1; i++) {
            int distance = restStop[i] - restStop[i-1] - 1;
            count += (distance / mid);
        }
        return count;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int L = Integer.parseInt(st.nextToken());
        
        restStop = new int[N+2];
        restStop[0] = 1;
        restStop[N+1] = L;
        st = new StringTokenizer(br.readLine());
        for (int i = 1; i <= N; i++) {
            restStop[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(restStop);

        int low = 0; 
        int high = L;
        while (low <= high) {
            int mid = (low + high) / 2;

            if (run(mid) <= M) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        System.out.println(low);
    }
}

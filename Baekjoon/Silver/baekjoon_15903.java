// 카드 합체 놀이

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class baekjoon_15903 {
        public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        PriorityQueue<Long> pq = new PriorityQueue<>();
        for (int i = 0; i < n; i++) {
            pq.add(Long.parseLong(st.nextToken()));
        }
        
        long tmpSum = 0;
        while (m > 0) { 
            tmpSum = pq.poll() + pq.poll();
            pq.add(tmpSum);
            pq.add(tmpSum);        
            m--;
        }

        long answerSum = 0;
        while (!pq.isEmpty()) {
            answerSum += pq.poll();
        }

        System.out.println(answerSum);
    }
}

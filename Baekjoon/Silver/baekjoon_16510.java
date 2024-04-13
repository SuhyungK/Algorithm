// Predictable Queue

package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

class Time implements Comparable<Time> {
    int workTime;
    int idx;

    Time(int workTime, int idx) {
        this.workTime = workTime;
        this.idx = idx;
    }

    @Override
    public int compareTo(Time t) {
        return this.workTime - t.workTime;
    }
}

public class baekjoon_16510 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] works = new int[N];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            works[i] = Integer.parseInt(st.nextToken());
        }

        PriorityQueue<Time> pq = new PriorityQueue<>();
        for (int i = 0; i < M; i++) {
            pq.add(new Time(Integer.parseInt(br.readLine()), i));
        }

        int idx = 0;
        int workSum = 0;
        int[] ans = new int[M];
        while (!pq.isEmpty()) {
            Time time = pq.poll();

            while (idx < N && time.workTime >= workSum + works[idx]) {
                workSum += works[idx];
                idx++;
            }
            ans[time.idx] = idx;
        }

        Arrays.stream(ans).forEach(System.out::println);
    }
}
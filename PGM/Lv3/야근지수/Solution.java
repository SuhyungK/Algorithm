package PGM.Lv3.야근지수;

import java.util.*;

public class Solution {
    public long solution(int n, int[] works) {

        PriorityQueue<Integer> workQueue = new PriorityQueue<>();
        for (int work : works) {
            workQueue.add(-work);
        }

        int cur;
        while (n > 0 && !workQueue.isEmpty()) {
            n--;
            cur = workQueue.poll() + 1;
            if (cur != 0) {
                workQueue.add(cur);
            }
        }

        long answer = 0L;
        while (!workQueue.isEmpty()) {
            answer += (long) Math.pow(workQueue.poll(), 2);
        }
        return answer;
    }
}
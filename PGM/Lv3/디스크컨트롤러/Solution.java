package PGM.Lv3.디스크컨트롤러;

import java.util.Arrays;
import java.util.PriorityQueue;

public class Solution {
    public static void main(String[] args) {
        Solution s = new Solution();
        s.solution(new int[][] {{0, 3}, {1, 9}, {2, 6}});
    }

    public int solution(int[][] jobs) {
        Arrays.sort(jobs, ((a, b) -> a[0] - b[0]));
        int answer = 0;
        int curTime = jobs[0][0]; // 시작 시간
        int curIdx = 1;
        PriorityQueue<Job> queue = new PriorityQueue<>();
        queue.add(new Job(jobs[0][0], jobs[0][1]));

        while (true) {
            while (curIdx < jobs.length && curTime >= jobs[curIdx][0]) {
                queue.add(new Job(jobs[curIdx][0], jobs[curIdx][1]));
                curIdx++;
            }

            if (queue.isEmpty()) {
                if (curIdx < jobs.length) {
                    queue.add(new Job(jobs[curIdx][0], jobs[curIdx][1]));
                    curTime = jobs[curIdx][0];
                    curIdx++;
                } else {
                    break;
                }
            }
            Job runJob = queue.poll();
            answer += (curTime - runJob.requestTime) + runJob.usedTime;
            curTime += runJob.usedTime;
        }
        return answer / jobs.length;
    }


    class Job implements Comparable<Job> {
        int requestTime;
        int usedTime;

        Job(int time1, int time2) {
            this.requestTime = time1;
            this.usedTime = time2;
        }
        @Override
        public int compareTo(Job other) {
            if (this.usedTime == other.usedTime) {
                return this.requestTime - other.requestTime;
            }
            return this.usedTime - other.usedTime;
        }
    }
}

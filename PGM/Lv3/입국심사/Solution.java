package PGM.Lv3.입국심사;

import java.util.*;

class Solution {
    public boolean binarySearch(long n, int[] times, long limitTime) {
        for (int time : times) {
            if (time > limitTime) break;
            n -= (limitTime / time);
            
            if (n <= 0) return true;
        }
        return n <= 0;
    }
    
    public long solution(int n, int[] times) {
        Arrays.sort(times);
        long maxTime = 1_000_000_000_000_000_000L - 1L;
        long minTime = 1L;
            
        long midTime;
        while (minTime <= maxTime) {
            midTime = (maxTime + minTime) / 2L;
            
            if (binarySearch(n, times, midTime)) {
                maxTime = midTime - 1L;
            } else {
                minTime = midTime + 1L;
            }
        }
        
        return minTime;
    }
}
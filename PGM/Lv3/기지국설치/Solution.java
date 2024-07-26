package PGM.Lv3.기지국설치;

public class Solution {
    public int solution(int n, int[] inputStations, int w) {
        int cur = 1, count = 0, idx = 0;
        int dis;
        int[] stations = new int[inputStations.length + 1];
        stations[stations.length - 1] = n + w + 1;
        System.arraycopy(inputStations, 0, stations, 0, inputStations.length);
        while (cur <= n) {
            if (!(stations[idx] - w <= cur && cur <= stations[idx] + w)) {
                dis = (int) Math.ceil((stations[idx] - cur - w) / (double) (2 * w + 1));
                count += dis;
            }
            cur = stations[idx] + w + 1;
            idx++;
        }
        return count;
    }
}

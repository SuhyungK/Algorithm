package PGM.Lv3.금과은운반하기;

class Solution {
    public long solution(int a, int b, int[] g, int[] s, int[] w, int[] t) {

        long maxTime = 4L * (long) Math.pow(10, 14);
        long minTime = 1L;
        while (minTime <= maxTime) {
            long midTime = (maxTime + minTime) / 2;

            if (search(a, b, a+b, g, s, w, t, midTime)) {
                maxTime = midTime - 1;
            } else {
                minTime = midTime + 1;
            }
        }

        return minTime;
    }

    public boolean search(int a, int b, int ab, int[] g, int[] s, int[] w, int[] t, long targetTime) {
        for (int i = 0; i < g.length; i++) {
            long roundTime = 2 * t[i]; // 왕복하는데 걸리는 시간
            long moveWeight = (targetTime / roundTime) * w[i]; // 시간 내 옮길 수 있는 최대 운반량
            if (targetTime % roundTime >= t[i]) {
                // 만약 편도로 한 번 더 갈 수 있다면 w[i] 만큼 더 옮길 수 있음
                moveWeight += w[i];
            }

            a -= Math.min(g[i], moveWeight);
            b -= Math.min(s[i], moveWeight);
            ab -= Math.min(g[i] + s[i], moveWeight);
        }

        return a <= 0 && b <= 0 && ab <= 0;
    }
}

package PGM.Lv3.광고삽입;

public class Solution {
    public String solution(String play_time, String adv_time, String[] logs) {
        int playTime = convert(play_time);
        int advTime = convert(adv_time);
        int[] views = new int[playTime + 2];

        String[] temp;
        for (String log : logs) {
            temp = log.split("-");
            views[convert(temp[0])]++;
            views[convert(temp[1])]--;
        }

        // 시청자 수 누적합
        for (int i = 1; i <= playTime; i++) {
            views[i] += views[i-1];
        }

        // 초기 누적합 값
        int startTime = 0;
        long maxView = 0;
        for (int i = startTime; i < advTime; i++) {
            maxView += views[i];
        }

        long curView = maxView;
        int maxStartTime = startTime;
        while (startTime + advTime <= playTime + 1) {
            curView = curView - views[startTime] + views[startTime + advTime];
            startTime++;
            if (curView > maxView) {
                maxStartTime = startTime;
                maxView = curView;
            }

        }
        return reverse(maxStartTime);
    }

    int convert(String input) {
        String[] time = input.split(":");
        return Integer.parseInt(time[0]) * 3600
                + Integer.parseInt(time[1]) * 60
                + Integer.parseInt(time[2]);
    }

    String reverse(int input) {
        int hour = input / 3600;
        input %= 3600;
        int minute = input / 60;
        input %= 60;
        return String.format("%02d", hour) + ":"
                + String.format("%02d", minute) + ":"
                + String.format("%02d", input);
    }
}
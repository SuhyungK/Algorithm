// 멀티탭 스케줄링

package Baekjoon.Gold;

import java.util.*;
import java.io.*;

public class baekjoon_1700 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] orders = new int[K];
        List<Queue<Integer>> orderInfo = new ArrayList<>();
        for (int i = 0; i <= K; i++) {
            orderInfo.add(new LinkedList<>());
        }
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < orders.length; i++) {
            orders[i] = Integer.parseInt(st.nextToken());
            orderInfo.get(orders[i]).add(i);
        }

        orderInfo.get(0).add(0);
        for (int i = 0; i <= K; i++) {
            orderInfo.get(i).add(K);
        }

        int[] taps = new int[N]; // 멀티탭
        boolean[] onOff = new boolean[K+1];
        
        int curNum;
        int changeIdx = 0;
        int answer = 0;
        int lastOrder;
        for (int i = 0; i < K; i++) {
            System.out.println(Arrays.toString(taps));
            curNum = orders[i];

            if (onOff[curNum]) {
                orderInfo.get(curNum).poll();
                continue;
            }

            lastOrder = 0;
            for (int j = 0; j < N; j++) {
                if (taps[j] == 0) {
                    changeIdx = j;
                    break;
                } else if (orderInfo.get(taps[j]).peek() > lastOrder){
                    System.out.println(orderInfo.get(taps[changeIdx]));
                    System.out.println(orderInfo.get(taps[j]));
                    changeIdx = j;
                    lastOrder = orderInfo.get(taps[changeIdx]).peek();
                }
            }

            if (taps[changeIdx] == 0) {
                // 빈 공간이 있는 것
                taps[changeIdx] = curNum;
                onOff[curNum] = true;
            } else if (taps[changeIdx] != curNum) {
                // 현재 탭에 꽂혀있지 않는 경우
                onOff[taps[changeIdx]] = false;
                onOff[curNum] = true;
                taps[changeIdx] = curNum;
                answer++;
            }
            orderInfo.get(curNum).poll();
        }
        System.out.println(Arrays.toString(taps));

        System.out.println(answer);
    }
}
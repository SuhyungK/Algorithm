package Baekjoon.Gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

class Meat implements Comparable<Meat>{
    int weight;
    int cost;

    Meat(int weight, int cost) {
        this.weight = weight;
        this.cost = cost;
    }

    @Override
    public int compareTo(Meat o) {
        if (this.cost != o.cost) return this.cost - o.cost;
        return o.weight - this.weight;
    }
}

public class baekjoon_2258 {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Meat[] meats = new Meat[N];
        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            meats[i] = new Meat(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }

        Arrays.sort(meats);

        int curCost = meats[0].cost; // 현재 기준이 되는 가격
        int buyCost = 0; // 구매 가격
        long totalWeight = 0; // 현재 가격으로 구매 가능한 무게
        int preWeight = 0; // 현재보다 바로 직전에 있는 낮은 가격 무게들의 합
        int answer = Integer.MAX_VALUE; // 최소 가격
        for (int i = 0; i < N; i++) {
            if (meats[i].cost != curCost) {
                curCost = meats[i].cost; // 기준이 되는 가격을 변경
                totalWeight = preWeight;
                buyCost = 0;
            }

            preWeight += meats[i].weight;
            buyCost += meats[i].cost;
            if (totalWeight < M) {
                totalWeight += meats[i].weight;
            }

            if (totalWeight >= M) {
                answer = Math.min(answer, buyCost);
            }
        }

        System.out.println(answer == Integer.MAX_VALUE ? -1 : answer);
    }
}
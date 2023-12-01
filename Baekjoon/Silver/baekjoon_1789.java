package Baekjoon.Silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class baekjoon_1789 {
    public static void main(String[] args) throws IOException{
        
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long S = Long.parseLong(br.readLine());

        long n = 1;
        long count = 0;
        while (true) {
            S -= n;
            if (S < 0) break;
            n++;
            count++;
        }
        System.out.println(count);
    }

}

// 수 이어가기

package Baekjoon.Silver;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.stream.Collectors;

public class baekjoon_2635 {
    static int N;
    static List<Integer> answer = new ArrayList<Integer>();
    
    static List<Integer> makeNumber(int secondNumber, List<Integer> numbers) {
        numbers.add(N);
        numbers.add(secondNumber);

        int index = 0;
        int nextNumber = N - secondNumber;
        while (nextNumber >= 0) {
            numbers.add(nextNumber);
            index++;
            nextNumber = numbers.get(index) - numbers.get(index+1);
        }
        
        if (numbers.size() > answer.size()) return numbers;
        return answer;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
            
        for (int i = 0; i <= N; i++) {
            answer = makeNumber(i, new ArrayList<>());
        }
        
        System.out.println(answer.size());
        System.out.println(answer.stream().map(Object::toString).collect(Collectors.joining(" ")));
    }
}

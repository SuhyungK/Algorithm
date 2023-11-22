import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    private static final int MAX_HEIGHT = 100_000_001;
    public static void main(String[] args) throws IOException {
        // 입력값 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] tower = new int[n+1];
        tower[0] = MAX_HEIGHT;
        for (int i = 0; i < n; i++) {
            tower[i+1] = Integer.parseInt(st.nextToken());
        }

        // 스택 생성
        Stack<Integer> stack = new Stack<>();
        stack.push(0);

        // tower 배열 값 스택에 저장
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            int now_height = tower[i+1];
            while(tower[stack.peek()] < now_height) {
                stack.pop();
            }
            answer[i] = stack.peek();
            stack.push(i+1);
        }


        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(answer[i] + " ");
        }
        System.out.println(sb.toString());
    }
}

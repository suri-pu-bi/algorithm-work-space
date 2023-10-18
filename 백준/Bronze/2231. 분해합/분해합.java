import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // 정수의 길이 -> String으로 바꿔서 계산
        int nSize = Integer.toString(n).length();
        int result = 0;

        // 분해합 결과 = N - 각 자릿수의 합
        // 분해합 결과가 최소가 될려면 각 자릿수의 합이 최대가 되어야함
        // 각 자릿수의 합이 최대일 떄 = 9 * (N의 길이)
        int start = n - (9 * nSize);
        for(int i= start; i < n; i++) {
            int number = i;
            int sum = i; // 각 자릿수 합 변수

            // 숫자가 크다고 각 자릿수 각각 구할 수 없는게 아니다!
            // 다음과 같이 구할 수 있다
            // 216 % 10 = 6, 216 / 10 = 21 -> 반복
            while (number != 0) {
                sum += number % 10; // 각 자릿수 더하기
                number /= 10;
            }

            if (sum == n) {
                result = i;
                break;
            }

        }

        System.out.println(result);
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int number = Integer.parseInt(br.readLine());

        int sum = 0;
        for (int i=0; i<number; i++) {
                // 입력 받은 문자열 한 줄 읽기
                StringTokenizer st = new StringTokenizer(br.readLine()); // 공백 기준으로 token들 저장
                int student = Integer.parseInt(st.nextToken());
                int apple = Integer.parseInt(st.nextToken());

                sum += (apple % student);

        }

        System.out.println(sum);


    }
}
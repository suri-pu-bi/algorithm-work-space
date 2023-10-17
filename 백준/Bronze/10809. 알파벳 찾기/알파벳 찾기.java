import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        // 알파벳 개수 : 26개
        char[] alpha = new char[26];

        // 알파벳 소문자로만 단어가 주어지므로
        // 아스키코드 소문자 : 97부터 시작
        for(int i=0; i<alpha.length; i++) {
            alpha[i] = (char) (97+i);
        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();

        for (int i=0; i<alpha.length;i++){
            // String에 Char문자가 포함되는지 확인: .indexOf
            // 있으면 처음 등장하는 위치 반환
            // 없으면 -1 반환
            // .equals: String 비교
            System.out.print(str.indexOf(alpha[i]));
            System.out.print(" ");
            }
        }


}
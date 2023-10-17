import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] basket = new int[n];
        for (int i=0; i<m; i++) {

            StringTokenizer st2 = new StringTokenizer(br.readLine());

            int firstBasket = Integer.parseInt(st2.nextToken());
            int lastBasket = Integer.parseInt(st2.nextToken());
            int ball = Integer.parseInt(st2.nextToken());

            for (int j=firstBasket-1; j<lastBasket; j++) {
                basket[j] = ball;
            }

        }

        for (int i=0; i<basket.length; i++){
            System.out.print(basket[i] + " ");
        }
    }
}

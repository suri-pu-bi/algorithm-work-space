import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	public static void main(String [] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int r = Integer.parseInt(st.nextToken());
		int c = Integer.parseInt(st.nextToken());

		int res = 0;
		while (N !=0) {
			N -= 1;

			// 제 1사분면
			if (r < Math.pow(2, N) && c < Math.pow(2, N)) {
				res += 0;
			}

			// 제 2사분면
			else if (r < Math.pow(2, N) && c >= Math.pow(2, N)) {
				res += (int)(Math.pow(2, N) * Math.pow(2, N));
				c -= (int) Math.pow(2, N);
			}

			// 제 3사분면
			else if (r >= Math.pow(2, N) && c < Math.pow(2, N)) {
				res += (int)(Math.pow(2, N) * Math.pow(2, N) * 2);
				r -= (int) Math.pow(2, N);
			}

			// 제 4사분면
			else {
				res += (int)(Math.pow(2, N) * Math.pow(2, N) * 3);
				r -= (int) Math.pow(2, N);
				c -= (int) Math.pow(2, N);
			}
		}
		System.out.println(res);
	}
}
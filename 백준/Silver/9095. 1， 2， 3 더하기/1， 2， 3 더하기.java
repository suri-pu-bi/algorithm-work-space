import java.io.*;

public class Main {
	static int[] dp;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		dp = new int[11]; // 정수가 11보다 작으므로 미리 크기를 정해놓으면 계속 안 만들어도됨
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 4;

		for(int i=4; i<11; i++){
			dp[i] = dp[i-3] + dp[i-2] + dp[i-1];
		}
		
		for(int i=0; i<T; i++) {
			int n = Integer.parseInt(br.readLine());
			System.out.println(dp[n]);

		}
	}
}

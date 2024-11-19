import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

// BFS와 DP 비교 필요
public class Main {
	static int[][] dp;
	static int n, m;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		dp = new int[n+1][m+1];

		// dp는 dp[n][m]까지 가야함. 범위 잘 생각하기
		for (int i=1; i<=n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=1; j<=m; j++) {
				dp[i][j] = Integer.parseInt(st.nextToken());
			}
		}


		// 대각선으로 가는 경로는 오른쪽, 아래를 거쳐서 가는 경우보다 항상 작음 -> 고려X
		// dp는 이전 지점의 값들을 불러오기 위함 -> 왼쪽, 위, 위왼 중 dp값 가져와서 큰 값을 자기자신과 더하기
		// (N,M)까지 하면 graph[N][M]이 정답이 됨

		for (int i = 1; i<=n; i++) {
			for (int j =1; j<=m; j++) {
				dp[i][j] += Math.max(dp[i-1][j], Math.max(dp[i][j-1], dp[i-1][j-1]));
			}
		}

		System.out.println(dp[n][m]);
	}
}
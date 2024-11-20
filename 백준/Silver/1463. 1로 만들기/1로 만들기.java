import java.io.*;

public class Main {
	static int minCnt = Integer.MAX_VALUE;
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());

		dfs(N, 0);
		System.out.println(minCnt);
	}
	// 완전탐색 DFS 해서 최솟값 계산
	static void dfs(int n, int cnt) {
		if (minCnt <= cnt) return;
		if (n == 1) {
			minCnt = Math.min(minCnt, cnt);
		} else { // if-else가 아닌 if문으로 연결되어있으므로 여러개로 가지치기 가능
			if(n%2 == 0) dfs(n/2, cnt+1);
			if(n%3 == 0) dfs(n/3, cnt+1);
			dfs(n-1, cnt+1);
		}
	}
}
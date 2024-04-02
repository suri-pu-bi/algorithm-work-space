import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

	static int n, m;
	static int cheese;
	static int[][] graph;
	static boolean[][] visited;
	static int[] dx = {-1, 1, 0, 0};
	static int[] dy = {0, 0, -1, 1};


	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		// 전체 치즈의 개수를 구한다.
		graph = new int[n][m];
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=0; j<m; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				// 전체 치즈의 개수를 구한다.
				if (graph[i][j] == 1) cheese++;
			}
		}

		int cheeseCnt = 0;
		int time = 0;
		while (cheese != 0) {
			cheeseCnt = cheese;
			time ++;
			visited = new boolean[n][m];
			bfs();
		}

		System.out.println(time);
		System.out.println(cheeseCnt);
	}

	public static void bfs() {
		Queue<int[]> q = new LinkedList<>();
		// 판 가장자리에는 치즈가 놓여있지않다고 했으므로 (0,0) 부터 시작
		q.offer(new int[] {0, 0});
		visited[0][0] = true;

		while(!q.isEmpty()) {
			int[] current = q.poll();

			for (int i =0; i < 4; i++) {
				int nx = current[0] + dx[i];
				int ny = current[1] + dy[i];

				if (nx >= 0 && nx < n && ny >= 0 && ny < m && !visited[nx][ny]) {
					visited[nx][ny] = true;
					if (graph[nx][ny] == 0) {
						// add : 큐가 꽉 찬 경우 에외 발생 시킴
						// offer : 추가 실패를 의미하는 false 리턴
						q.add(new int[] {nx, ny});
					} else {
						cheese --;
						// 이미 방문했으므로 치즈를 0으로 바꿔도 탐색하지 않는다.
						graph[nx][ny] = 0;
					}
				}
			}
		}

	}
}
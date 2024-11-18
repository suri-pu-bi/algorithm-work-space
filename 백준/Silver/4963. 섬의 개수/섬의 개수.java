import java.io.*;
import java.util.*;
public class Main {
	static int[][] map; // 길이가 고정되어있으므로 배열로
	static int w, h;
	// BFS 호출할 때마다 매번 dx, dy 생성할 필요 없으므로 전역으로 선언
	static int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
	static int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};

	// 방문했는지 BFS 함수 여러번 호출할 때마다 초기화되면 안되므로 전역으로 선언
	static boolean[][] visited;
	public static void main(String[] args) throws IOException {
		// while문에 넣으면 반복할 때마다 객체를 만드므로 비효율적
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		while (true) {
			st = new StringTokenizer(br.readLine());

			w = Integer.parseInt(st.nextToken());
			h = Integer.parseInt(st.nextToken());

			if (w == 0 && h == 0) {
				break;
			}

			map = new int[h][w];
			visited = new boolean[h][w]; // BFS 안에서 초기화 X

			for (int i=0; i<h; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j=0; j<w; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}

			int result = 0;
			for (int i=0; i<h; i++) {
				for (int j=0; j<w; j++) {
					if (map[i][j] == 1 && !visited[i][j]) { // 이미 BFS에서 방문한 노드는 또 BFS를 호출하면 안됨
						bfs(i, j);
						result ++;
					}
				}
			}
			System.out.println(result);

		}
	}

	static void bfs(int i, int j) {
		Queue<int[]> q = new LinkedList<>();
		visited[i][j] = true;
		q.add(new int[]{i, j});

		while (!q.isEmpty()) {
			int[] cur = q.poll();
			for (int k=0; k<8; k++) {
				int nx = cur[0] + dx[k], ny = cur[1] + dy[k];

				if (nx >= 0 && ny >= 0 && nx < h && ny < w){
					if (map[nx][ny] == 1 && !visited[nx][ny]) {
						q.offer(new int[]{nx, ny});
						visited[nx][ny] = true;
					}
				}
			}

		}
	}
}

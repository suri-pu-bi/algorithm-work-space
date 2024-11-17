import java.io.*;
import java.util.*;

public class Main {
	// 양방향 그래프이어야함 : 자식 -> 부모로 이동 가능, 인덱스별로 연결된 노드들을 그래프에 넣기 예) 1 인덱스 : [2, 3, 4]
	static List<Integer>[] relation; // 인덱스 길이는 고정, 연결된 노드들 길이는 가변
	static boolean[] visited;
	static int result = -1; // 관계가 없을 때 기본값 -1
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int x = Integer.parseInt(st.nextToken());
		int y = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(br.readLine());

		relation = new ArrayList[n+1]; // 고정길이
		visited = new boolean[n+1];
		for(int i = 0; i < n+1; i++) {
			relation[i] = new ArrayList<>(); // 가변길이
		}

		for (int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int p = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			// 양방향 그래프
			relation[p].add(c);
			relation[c].add(p);
		}

		dfs(x, y, 0);
		System.out.println(result);
	}

	static void dfs(int start, int end, int cnt){
		if (start == end) { // 목표 지점 도착 (종료 조건)
			result = cnt;
			return;
		}

		visited[start] = true;
		for(int i=0; i<relation[start].size(); i++){
			int next = relation[start].get(i);
			if(!visited[next]) {
				dfs(next, end, cnt+1); // depth가 깊어질 때마다 카운트를 세어주기
			}
		}
	}
}
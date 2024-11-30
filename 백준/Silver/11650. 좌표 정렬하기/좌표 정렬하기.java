import java.io.*;
import java.util.*;

public class Main {
	static int[][] dots;
	static int N;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		dots = new int[N][2];
		StringTokenizer st;

		for (int i=0; i<N; i++) {
			st = new StringTokenizer(br.readLine());
			dots[i][0] = Integer.parseInt(st.nextToken());
			dots[i][1] = Integer.parseInt(st.nextToken());
		}

		sort();
		print();

	}

	static void sort() {
		Arrays.sort(dots, (e1, e2) -> { // dots의 배열의 두 개 요소
			if (e1[0] == e2[0]) { // 첫번째 x값이 같으면 두번째 y값을 기준으로 오름차순 정렬
				// Compartor 비교방식 : 반환 값이 양수면, 첫 번째 요소가 두 번째 요소보다 크다고 판단 -> 순서를 바꿈
				// 반환 값이 음수면, 첫 번째 요소가 두 번째 요소보다 작다고 판단 -> 순서 유지
				// 반환 값이 0이면, 같다고 판단 -> 순서 유지
				return e1[1] - e2[1];
			} else { // 다르면 첫번째 x값을 기준으로 오름차순 정렬
				return e1[0] - e2[0];
			}
		});
	}

	static void print() {
		StringBuilder sb = new StringBuilder();
		for(int i=0; i<N; i++) {
			sb.append(dots[i][0]).append(" ").append(dots[i][1]).append('\n');
		}
		System.out.println(sb);
	}
}

import java.io.*;
import java.util.*;

public class Main {
	public static boolean[] prime;
	static int i;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int M = Integer.parseInt(st.nextToken());
		int N = Integer.parseInt(st.nextToken());

		prime = new boolean[N+1]; // 0 ~ N
		getPrime();

		StringBuilder sb = new StringBuilder();

		for (int i = M; i<= N; i++) {
			// false = 소수
			if(!prime[i]) sb.append(i).append('\n');
		}

		System.out.println(sb);

	}
	// 에라토스테네스의 체
	// p와 q가 N의 약수라면, p와 q 중 하나는 반드시 루트 N보다 작거나 같을 수 밖에 없다!
	// k=2부터 루트 N 이하까지 반복하여 자연수들 중 k를 제외한 k의 배수들을 제외시키는 알고리즘
	static void getPrime() {
		// boolean 배열 초기값이 false이므로 true: 소수 아님 false: 소수로 설정
		prime[0] = prime[1] = true; // 0, 1

		for (int i=2; i<= Math.sqrt(prime.length); i++) {
			// 이미 소수가 아니라고 체크가 됐다면 다음 반복문으로 점프
			if (prime[i]) continue;
			// i를 제외한 i의 배수들을 소수가 아니라고 체크
			for(int j=i*i; j<prime.length; j+= i) {
				prime[j] = true;
			}
		}
	}
    
    /* 배열에서 특정 숫자 포함 여부 확인
		static int i;
		IntStream.of(nums).anyMatch(x -> x == i)

	 */
}
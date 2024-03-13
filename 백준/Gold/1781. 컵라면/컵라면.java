import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.util.PriorityQueue;

public class Main {

    static int n;
    static int[][] problems;

    static int result;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        problems = new int[n][2];


        for(int i=0; i<n; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            problems[i][0] = Integer.parseInt(st.nextToken());
            problems[i][1] = Integer.parseInt(st.nextToken());
        }

        Arrays.sort(problems, Comparator.comparingInt((int[] num) -> num[0])
                .thenComparingInt(num -> num[1]));


        // 우선순위가 낮은 숫자인 int형 우선순위큐 (최소힙)
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int[] i : problems) {
            pq.add(i[1]);
            if (i[0] < pq.size()) {
                pq.poll();
            }
        }

        while (!pq.isEmpty()) {
            result += pq.poll();
        }

        System.out.println(result);
    }
}

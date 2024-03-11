
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    static int n;
    static int[] weight;
    static int target;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        weight = new int[n];
        for (int i=0; i<n; i++){
            weight[i] = Integer.parseInt(st.nextToken());
        }

//        System.out.println(n);
//        System.out.println(Arrays.toString(weight));

        Arrays.sort(weight);

        target = 1;
        for (int i=0; i<n; i++) {
            if (target < weight[i]) {
                break;
            }
            target += weight[i];
        }

        System.out.println(target);

    }

}

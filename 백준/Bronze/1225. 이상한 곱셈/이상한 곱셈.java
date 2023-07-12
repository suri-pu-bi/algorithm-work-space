import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String[] arr1 = st.nextToken().split("");
        String[] arr2 = st.nextToken().split("");

        long result = 0L;
        for (String i : arr1){
            for (String j : arr2){
                result += (Integer.parseInt(i) * Integer.parseInt(j));
            }
        }

        System.out.println(result);

    }


}
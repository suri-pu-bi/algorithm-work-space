import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int firstOut = Integer.parseInt(st.nextToken());
        int firstIn = Integer.parseInt(st.nextToken());
        int value = firstIn;
        int maxValue = firstIn;

        for (int i=0; i<9; i++){
            st = new StringTokenizer(br.readLine());
            int out = Integer.parseInt(st.nextToken());
            int in = Integer.parseInt(st.nextToken());
            value = value - out + in;

            if (maxValue < value){
                maxValue = value;
            }

        }

        System.out.println(maxValue);


        }
    }

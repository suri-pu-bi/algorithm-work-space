import java.io.*;


public class Main {
    public static void main(String[] args) {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        StringTokenizer st = new StringTokenizer(br.readLine()); // 공백 기준으로 입력받을 때 사용

        try {
            String str = "";
                int n = Integer.parseInt(br.readLine());
                String numbers = br.readLine();
                int result = 0;

                for (String t : numbers.split("")) {
                    result += Integer.parseInt(t);
                }

                System.out.println(result);

        }

        catch (IOException e){
            throw new RuntimeException(e);
        }


    }
}

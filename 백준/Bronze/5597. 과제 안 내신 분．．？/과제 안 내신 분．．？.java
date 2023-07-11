import java.io.*;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int[] students = new int[31];


        for (int i = 0; i < 28; i++) { // 출석번호가 index가 됨
            students[sc.nextInt()] = 1;
        }


        for (int i = 1; i <= 30; i++) {
            // 출석번호가 index인데 index가 작은 것부터 for문을 돌기 때문에 정렬 등 필요X
            if (students[i] == 0) {
                System.out.println(i);
            }
        }


    }
}
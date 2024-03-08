
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static char[][] graph;
    static int r;
    static int c;
    static int count;
    static int[][] visited;
    static int[] dx;
    static int[] dy;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        graph = new char[r][c];
        for (int i=0; i<r; i++){
            graph[i] = br.readLine().toCharArray();
        }

        dx = new int[]{-1, 0, 1};
        dy = new int[]{1, 1, 1};

        visited = new int[r][c];
        for (int i = 0; i<r; i++){
            for (int j = 0; j<c; j++) {
                visited[i][j] = -1;
            }
        }

        for(int i=0; i<r; i++){
            if (dfs(i, 0)) {
                count++;
            }
        }

        System.out.println(count);

    }

    public static boolean dfs(int x, int y) {
        if (y == c-1) {
            return true;
        }

        for (int i=0; i<3; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if (0 <= nx &&  nx < r && 0 <= ny && ny < c) {
                if (graph[nx][ny] != 'x' && visited[nx][ny] == -1) {
                    visited[nx][ny] = 1;
                    if (dfs(nx, ny)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }
}

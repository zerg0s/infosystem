import java.util.Scanner;

public class Draughts{

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.println("Ввод");
        int x0 = in.nextInt();
        int y0 = in.nextInt();
        int x1 = in.nextInt();
        int y1 = in.nextInt();

        System.out.println();
        System.out.println("Вывод");
        if (y1 <= y0 | (x0 + y0) % 2 != (x1 + y1) % 2) {
            System.out.println("NO");
        } else if (x0 - (y1 - y0) <= x1 & x1 <= x0 + (y1 - y0)) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }
}

import java.util.Scanner;

public class SumOfNeighbors {

    static Scanner in = new Scanner(System.in);
    static final String ERROR_MESSAGE = "ERROR";
    static final Integer NEXT = 1;

    public static void main(String[] args) {

        try {
            Integer n = in.nextInt();
            Integer sum = 0;
            in.nextLine();

            for (int i = 1; i < n; i++) {
                sum += i * (i + NEXT);
                System.out.print(i + "*" + (i + NEXT));

                if (i < n - NEXT) {
                    System.out.print("+");
                }
            }

            System.out.print("=" + sum);
        } catch (Exception e) {
            System.out.print(ERROR_MESSAGE);
        }
    }
}


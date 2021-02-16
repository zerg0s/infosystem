
import java.util.Scanner;

public class Main {
    private static final int  MKAD = 109;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int speed = sc.nextInt();
        int time = sc.nextInt();
        System.out.println((speed*time) % MKAD);
    }
}


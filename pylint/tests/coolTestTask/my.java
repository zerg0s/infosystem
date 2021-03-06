import java.util.Scanner;

public class HelloWorld {
    public static void main(String[] var0) {
		Scanner in = new Scanner(System.in);
		int a = in.nextInt();
		int sum1 = 0;
		sum1 += a % 2;
		a = a / 2;
		sum1 += a % 2;
		a /= 2;
		sum1 += a % 2;
		a /= 2;
		sum1 += a % 2;
		System.out.println("Количество единиц в двоичном представлении = " + sum1);
    }
}
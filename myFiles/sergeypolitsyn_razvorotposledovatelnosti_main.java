package ru.mai;

import java.util.Scanner;

public class Main {
    static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        inputNum(); // выводит числа в обратной последовательности
    }

    private static void inputNum() {
        long num = in.nextLong(); // ввод числа

        /*
         * Если введённое число не равно нулю, то вызывается эта же функция с повторным вводом числа
         * Иначе вся рекурсия останавливается, и все введенные числа выводятся в обратном порядке
         */
        if (num != 0) {
            inputNum();
        }
        System.out.println(num); // вывод числа
    }
}

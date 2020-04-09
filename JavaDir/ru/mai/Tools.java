package ru.mai;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Tools {

    static final byte EMPTY = 0;

    private static Scanner in = new Scanner(System.in);

    public static String[] inputingStrings(String[] strs) {

        for (int i = 0; i < strs.length; ++i) {
            try {
                strs[i] = in.next();
            } catch (Exception e) {
                throw e;
            }
        }

        return strs;
    }

    public static byte getQuantityOfStrings() {

        try {
            return in.nextByte();
        } catch (InputMismatchException e) {
            return EMPTY;
        }
    }
}

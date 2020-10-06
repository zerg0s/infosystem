package ru.mai;

import java.util.Scanner;

public class ReverseAFragment {
    static Scanner cs = new Scanner(System.in);
    static StringBuilder sbResult;

    public static void main(String[] args) {
        sbResult = new StringBuilder();
        String line = cs.nextLine();
        int first = line.indexOf('h');
        int last = line.lastIndexOf('h');
        int i = 0;
        while (i < line.length()) {
            if (i <= first || i >= last) {
                sbResult.append(line.charAt(i));
            }
            if (i > first && i < last) {
                sbResult.append(line.charAt(last + first - i));
            }
            i++;
        }
        System.out.println(sbResult.toString());
    }
}

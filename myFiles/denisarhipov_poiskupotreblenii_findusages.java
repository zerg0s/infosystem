package ru.mai;

import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class FindUsages {

    private static Scanner in = new Scanner(System.in);

    public static void main(String[] args) {
        String line = in.nextLine();
        String pattern = "[Вв]рем(я|ени|енем)";
        Pattern p = Pattern.compile(pattern);
        Matcher matcher = p.matcher(line);
        boolean hasWord = false;
        while (matcher.find()) {
            System.out.println(line.substring(matcher.start(), matcher.end()));
            hasWord = true;
        }
        if (!hasWord) {
            System.out.println("No");
        }
    }
}

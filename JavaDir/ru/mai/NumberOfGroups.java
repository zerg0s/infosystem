package ru.mai;

import java.util.*;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static ru.mai.Tools.getQuantityOfStrings;
import static ru.mai.Tools.inputingStrings;

public class NumberOfGroups {

    static final byte EMPTY = 0;
    static final String regex = "М3О-([\\d]{3})Б-(14|15|16|17|18|19)";
    static Scanner in = new Scanner(System.in);
    static Pattern pattern = Pattern.compile(regex);

    public static void main(String args[]) {

        byte quantityOfStrings = getQuantityOfStrings();

        String[] strs = new String[quantityOfStrings];

        strs = inputingStrings(strs);

        for (String str : correctGroups(strs)) {
            System.out.println(str);
        }

    }

    private static ArrayList<String> correctGroups(String[] strs) {
        Matcher matcher;
        ArrayList<String> matches = new ArrayList<String>();

        for (String str : strs) {
            matcher = pattern.matcher(str);
            if (matcher.find()) matches.add(str);
        }

        return matches;
    }

}

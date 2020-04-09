package ru.mai;

import java.util.Scanner;

public class Desks {
    static Scanner cs = new Scanner(System.in);

    public static void main(String[] args) {
        try {
            int numberOfStudents1 = cs.nextInt();
            int numberOfStudents2 = cs.nextInt();
            int numberOfStudents3 = cs.nextInt();
            int numberOfDesks = (int) (Math.ceil(numberOfStudents1 / 2.)
                                + Math.ceil(numberOfStudents2 / 2.)
                                + Math.ceil(numberOfStudents3 / 2.));
            System.out.println(numberOfDesks);

        } catch (Exception ex) {
            System.out.println("ERROR");
        }
    }
}
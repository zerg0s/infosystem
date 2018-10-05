package com.prog.systems;

import java.io.*;


public class zadanie4 {
    public static int length[] = new int[3];
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        int l[] = new int[3];
        int r[] = new int[3];
        for (int i = 0; i < 3; i++) {
            int n = i + 1;
            System.out.println("Введите концы " + n + " спички через enter");
            l[i] = Integer.parseInt(bufferedReader.readLine());
            r[i] = Integer.parseInt(bufferedReader.readLine());
            length[i] = r[i] - l[i];
        }
        if (r[0] >= l[1] && r[1] >= l[2]){
            System.out.println(0);
        }else{
            if((l[2] - r[1]) <= length[0]){
                System.out.println("1");
            }else{
                if((l[1] - r[0]) <= length[2]){
                    System.out.println("3");
                }else{
                    System.out.println("-1");
                }
            }

        }
    }
}

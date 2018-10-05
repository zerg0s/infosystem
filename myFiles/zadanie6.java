package com.prog.systems;

import java.io.*;


public class zadanie6 {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        double x,y;
        x = Double.parseDouble(bufferedReader.readLine());
        y = Double.parseDouble(bufferedReader.readLine());
        int count = 0;
        while (x < y){
            x *= 1.1;
            count++;
        }
        System.out.println(count);
    }
}

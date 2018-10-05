package com.prog.systems;

import java.io.*;


public class zadanie8 {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        int x = -1;
        int firstMax = 0, secondMax = 0;
        while(x != 0){
            x = Integer.parseInt(bufferedReader.readLine());
            if(x >= firstMax){
                secondMax = firstMax;
                firstMax = x;
            }
        }
        System.out.println("first Maximum = " + firstMax + " second Maximum = " + secondMax);
    }
}

package com.prog.systems;

import java.io.*;


public class zadanie7 {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        int x = Integer.parseInt(bufferedReader.readLine());
        int y = Integer.parseInt(bufferedReader.readLine());
        while (x != y){
            if ((x%2 == 0) && (x/2 > y)){
                System.out.println(":2");
                x = x / 2;
            }else{
                System.out.println("-1");
                x--;
            }
        }
    }



}

package com.prog.systems;

import java.io.*;


public class zadanie5 {
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        double a,b,c,d;
        System.out.println("Ввведите a");
        a = Double.parseDouble(bufferedReader.readLine());
        System.out.println("Ввведите b");
        b = Double.parseDouble(bufferedReader.readLine());
        System.out.println("Ввведите c");
        c = Double.parseDouble(bufferedReader.readLine());
        System.out.println("Ввведите d");
        d = Double.parseDouble(bufferedReader.readLine());

        if(a==0){
            System.out.println("INF");
        }else{
            if((-b/a) == (-d/c)){
                System.out.println("NO");
            }else{
                System.out.println(-b/a);
            }
        }
    }
}

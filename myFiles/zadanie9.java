package com.prog.systems;

import java.io.*;


public class zadanie9 {
    public static int count = 3;
    public static int lastLocalMax = 0;
    public static int minDistance = 0;
    public static int first = 0;
    public static int second = 0;
    public static int third = 0;
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        first = Integer.parseInt(bufferedReader.readLine());
        second = Integer.parseInt(bufferedReader.readLine());
        third = Integer.parseInt(bufferedReader.readLine());
        check();
        int x = -1;
        while (x != 0){
            count++;
            x = Integer.parseInt(bufferedReader.readLine());
            if (x == 0) break;
            next(x);
            check();
        }
        System.out.println("Minimal distance of local Maximumus = " + minDistance);
    }
    public static void next(int x){
        first = second;
        second = third;
        third = x;

    }

    public static void check(){
        if ((second > first) && (second > third)){
            if(lastLocalMax == 0){
                lastLocalMax = count - 1;
            }else{
                if(minDistance == 0){
                    minDistance = count - 1 - lastLocalMax;
                    lastLocalMax = count -1;
                }else{
                    if(minDistance > count - 1 - lastLocalMax){
                        minDistance = count - 1 - lastLocalMax;
                        lastLocalMax = count -1;
                    }else{
                        lastLocalMax = count -1;
                    }
                }
            }
        }
    }

}

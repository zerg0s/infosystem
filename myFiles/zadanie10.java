package com.prog.systems;

import java.io.*;

public class zadanie10 {
    public static int count = 0;
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        int x = Integer.parseInt(bufferedReader.readLine());
        while (x != 0){
            check(x);
            x--;
        }
        System.out.println(count);
    }
    public static void check(int x){
        if (x / 10000 > 0){
            if((x/10000 == x%10) && (x/1000%10 == x/10%10)) count++;
        }else{
            if (x / 1000 > 0){
                if ((x/1000 == x%10) && (x/100%10 == x/10%10)) count++;
            }else{
                if (x / 100 > 0){
                    if (x / 100 == x % 10) count++;
                }else{
                    if (x / 10 > 0){
                        if (x / 10 == x % 10) count++;
                    }else{
                        if (x < 10) count++;
                    }
                }
            }
        }
    }
}

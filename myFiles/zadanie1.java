package com.prog.systems;

import java.io.*;
import static java.lang.Math.abs;

public class zadanie1 {

    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        int mass[] = new int[4];
        System.out.println("Введите номера сток и столбцов в порядке X1,Y1 и X2,Y2. После каждого числа enter.");
        for (int i = 0; i < 4; i++) {
            mass[i] = Integer.parseInt(bufferedReader.readLine());
        }
        solve(mass[0],mass[1],mass[2],mass[3]);
    }

    public static void solve(int x1, int y1, int x2, int y2) {
        if(near(x1,x2) && (near(y1,y2))){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }

    public static boolean near(int a, int b){
        if((abs(a-b) == 1) || (a-b == 0)){
            return true;
        }else{
            return false;
        }

    }
}
package com.prog.systems;

import java.io.*;
import java.util.Arrays;
import java.util.Collections;


public class zadanie2 {
    public static int[] indexes = new int[3];
    public static Integer sklad[] = new Integer[3];
    public static Integer box[] = new Integer[3];
    public static void main(String[] args) throws IOException {
        InputStream inputStream = System.in;
        Reader inputStreamReader = new InputStreamReader(inputStream);
        BufferedReader bufferedReader = new BufferedReader(inputStreamReader);
        System.out.println("Введите параметры склада через enter");
        for (int i = 0; i < 3; i++) {
            sklad[i] = Integer.parseInt(bufferedReader.readLine());
        }
        System.out.println("Введите параметры коробок через enter");
        for (int i = 0; i < 3; i++) {
            box[i] = Integer.parseInt(bufferedReader.readLine());
        }
        Arrays.sort(sklad, Collections.reverseOrder());
        Arrays.sort(box, Collections.reverseOrder());
        Integer copyOfSklad[] = new Integer[3];
        for (int i = 0; i < sklad.length; i++) {
            copyOfSklad[i] = sklad[i];
        }
        if((sklad[0] >= box[0]) && (sklad[1] >= box[1]) && (sklad[2] >= box[2])){
            Integer ostAll[][] = new Integer[3][3];
            for (int j = 0; j < 3; j++) {
                for (int i = 0; i < 3; i++) {
                    ostAll[i][j] = sklad[i]%box[j];;
                }
            }
            side(ostAll);
            solve();
        }else{
            System.out.println("0");
        }
    }

    public static void minIndexOf(int ost[]){
        int minIndex = 0;
        for (int i = 1; i < ost.length; i++) {
            if(ost[i] < ost[minIndex]){
                minIndex = i;
            }
        }
        indexes[0] = minIndex;
    }
    public static void minIndexOf(int ost[], int index){
        int k = 10,n = 10;
        for (int i = 0; i < 3; i++) {
            if ((i != indexes[0]) && (i != k) && (n != 11)){
                k = i;
                n = 11;
            }
            if ((i != indexes[0]) && (i != k) && (i != n)){
                n = i;
            }
        }
        if (ost[k] <= ost[n]){
            indexes[1] = k;
            indexes[2] = n;
        }else{
            indexes[1] = n;
            indexes[2] = k;
        }
    }
    public static void side(Integer[][] ostall){
        int ost[] = new int[3];
        for (int j = 0; j < 3; j++) {
            for (int i = 0; i < 3; i++) {
                ost[i] = ostall[i][j];
            }
            if (j==0) {
                minIndexOf(ost);
            }else{
                minIndexOf(ost, indexes[j-1]);
            }
        }
    }
    public static void solve(){
        int mass = 1;
        for (int i = 0; i < 3; i++) {
            mass *= sklad[indexes[i]] / box[i];
        }
        System.out.println(mass + " - количество коробок");
    }


}

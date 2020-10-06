package ru.mai.CivilDefense;

import java.util.*;

class Village {

    public Byte position;
    public Integer shelter = 0;
}

public class CivilDefense {

    static Scanner in = new Scanner(System.in);
    static final byte OFFSET = 1;


    public static void main(String[] args) {

        int quantityOfVillages = in.nextInt();

        ArrayList<Village> villages = new ArrayList<Village>(quantityOfVillages);

        for (int i = 0; i < quantityOfVillages; ++i) {
            Village village = new Village();
            village.position = in.nextByte();
            villages.add(village);
        }

        int quantityOfDefenders = in.nextInt();

        HashMap<Byte, Integer> defenders = new HashMap<Byte, Integer>();
        ArrayList<Byte> buffDefenders = new ArrayList<Byte>(quantityOfDefenders);

        for (int i = 0; i < quantityOfDefenders; ++i) {
            Byte buff = in.nextByte();
            defenders.put(buff, i);
            buffDefenders.add(buff);
        }

        Collections.sort(buffDefenders);

        Iterator<Village> iterVil = villages.iterator();

        for (int i = 0; i < quantityOfVillages; ++i) {
            Village village = iterVil.next();
            village.shelter = defenders.get(buffDefenders.get(SmartCollections.indexedBinarySearch(buffDefenders, village.position))) + OFFSET;
        }

        for (Village res : villages) {
            System.out.print(res.shelter + " ");
        }
    }
}

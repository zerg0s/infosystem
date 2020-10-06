package ru.mai.CivilDefense;

import java.util.Collections;
import java.util.InputMismatchException;
import java.util.List;

public class SmartCollections {

    public static <T>
    int indexedBinarySearch(List<? extends Comparable<? super T>> list, T key) {
        int low = 0;
        int high = list.size() - 1;

        do {
            int mid = (low + high) >>> 1;
            Comparable<? super T> midVal = list.get(mid);
            int cmp = midVal.compareTo(key);

            if (cmp < 0) {
                low = mid + 1;
            } else if (cmp > 0) {
                high = mid - 1;
            } else {
                return mid; // key found
            }
        } while (low <= high);

        try {
            Comparable<? super T> lowValue = list.get(low);
            Comparable<? super T> highValue = list.get(high);

            int cmp1 = lowValue.compareTo(key);
            int cmp2 = highValue.compareTo(key);

            if (Math.abs(cmp1) > Math.abs(cmp2)) {
                return high;
            }
        } catch (Exception e) {

        }

        if (low == list.size()) {
            return low - 1;
        } else {
            return low; // key not found
        }
    }
}


package com.example.vargenerator.api.controller;

import java.util.*;

/**
 3
 4
 7
 10


 1 => 1
 1

 2 => 2
 11
 2

 3 => 4
 111
 12
 21
 3

 4 => 7
 1111
 112
 121
 211
 22
 13
 31

 5 => 13
 11111
 1112
 1121
 1211
 2111
 122
 212
 221
 113
 131
 311
 23
 32


 6 => 24
 111111
 11112
 11121
 11211
 12111
 21111
 1113
 1131
 1311
 3111
 1122
 1212
 1221
 2112
 2121
 2211
 222
 123
 132
 213
 231
 312
 321
 33


 */
// https://www.acmicpc.net/problem/9095
public class Solve {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int length = scanner.nextInt();
        int[] box = new int[12];
        box[0] = 0;
        box[1] = 1;
        box[2] = 2;
        box[3] = 4;
        for (int i = 4; i <= 11; i++) {
            box[i] = box[i - 3] + box[i - 2] + box[i - 1];
        }

        List<Integer> arr = new ArrayList<>();
        for(int i = 0; i < length; i++) {
            int value = scanner.nextInt();

            System.out.println(box[value]);
        }



    }
}

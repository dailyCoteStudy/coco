package com.example.vargenerator.api.controller;

import java.util.Arrays;
import java.util.Scanner;

/**
 * 55-50+40
 * 10+20+30+40
 * <p>
 * 55-50+40-30
 */

//https://www.acmicpc.net/problem/1541
public class Solve {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        String value = scanner.next();
//        value = "55-50+40-30+90"
//        value = "55+11+44+19" //[55,11,44,19]


        if (value.contains("-")) {
//            55+90-50+40-30+90
            String[] minusBox = value.split("-"); // [55+90, 50+40, 30+90]
            int result = 0;

            String[] first = minusBox[0].split("\\+"); //[55, 90]
            for (String s : first) {
                result += Integer.parseInt(s);
            }
            result = 145

            for (int i = 1; i < minusBox.length; i++) {
                /**
                 * i = 1;  split = [50, 40]
                 * i = 2;  split = [30, 90]
                 *
                 */
                String[] split = minusBox[i].split("\\+");
                int minusValue = 0;
                for (String s : split) {
                    minusValue += Integer.parseInt(s);
                }

                result -= minusValue;
            }
            System.out.println(result);


        } else {
            String[] split = value.split("\\+"); //[55,11,44,19]
            System.out.println(Arrays.stream(split).mapToInt(Integer::parseInt).sum());
        }

    }
}
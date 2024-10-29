import java.util.Scanner;

/**
 3
 https://www.acmicpc.net/problem/1436

 숌

 1 = 666
 2 = 1666
 3 = 2...
 4 = 3
 ..
 7= 6666
 8 = 7666
 
 */
public class Solve {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int value = scanner.nextInt(); // 6


        String result = "666";


        while (true) {
            if (result.contains("666")) {
                value--;
                System.out.println("result = " + result);
            }
            System.out.println(value);
            if (value == 0) {
                break;
            } else {
                result = String.valueOf(Integer.parseInt(result) + 1);
            }
        }
        System.out.println(result);
    }
}

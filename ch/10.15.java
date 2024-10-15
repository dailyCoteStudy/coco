
import java.util.*;

/**
 5
 6 3 2 10 -10
 8
 10 9 -5 2 3 4 5 -10

 https://www.acmicpc.net/problem/10815
 */
public class Solve {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int myLength = scanner.nextInt();

        Map<Integer, Integer> myBox = new HashMap<>();
        for (int i = 0; i < myLength; i++) {
            myBox.put(scanner.nextInt(),0);
        }

        int yourLength = scanner.nextInt();
        List<Integer> resultBox = new ArrayList<>();
        for (int i = 0; i < yourLength; i++) {
            int value = scanner.nextInt();
            if (myBox.containsKey(value)) {
                resultBox.add(1);
            } else {
                resultBox.add(0);
            }
        }
        for (Integer box : resultBox) {
            System.out.println(box);
        }



    }
}

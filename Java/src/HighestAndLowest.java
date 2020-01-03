import java.util.ArrayList;
import java.util.List;

public class HighestAndLowest {
    public static String highAndLow(String numbers) {
        if (numbers.length() < 1) {
            return null;
        }
        int lowNum = Integer.MAX_VALUE;
        int highNum = Integer.MIN_VALUE;
        List<Integer> numList = new ArrayList<Integer>();
        for (String i: numbers.split(" ")) {
            numList.add(Integer.parseInt(i));
        }
        for (int i: numList) {
            if (i < lowNum) {
                lowNum = i;
            }
            if (i > highNum) {
                highNum = i;
            }
        }
        return Integer.toString(highNum) + " " + Integer.toString(lowNum);
    }
    public static void main(String[] args) {
        System.out.println(HighestAndLowest.highAndLow(""));
        System.out.println(HighestAndLowest.highAndLow("1"));
        System.out.println(HighestAndLowest.highAndLow("1 2 3 4 5"));
        System.out.println(HighestAndLowest.highAndLow("1 -1 9 5 -2"));
    }

}

import java.util.ArrayList;
import java.util.List;

public class AreTheyTheSame {
    public static boolean comp(int[] a, int[] b) {
        List<Integer> c = new ArrayList<Integer>();
        for (int i: a) {
            c.add(i * i);
        }
        for (int j: b) {
            if (!c.contains(j)) {
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) {
        int[] a = new int[]{121, 144, 19, 161, 19, 144, 19, 11};
        int[] b = new int[]{121, 14641, 20736, 361, 25921, 361, 20736, 361};
        System.out.println(AreTheyTheSame.comp(a, b));
    }

}

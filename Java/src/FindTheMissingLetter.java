import java.util.HashMap;
import java.util.Map;

public class FindTheMissingLetter {
    public static char findMissingLetter(char[] array) {
        Map<Character, Integer> alphabetDict = new HashMap<Character, Integer>() {{
            put('a', 1);
            put('A', 1);
            put('b', 2);
            put('B', 2);
            put('c', 3);
            put('C', 3);
            put('d', 4);
            put('D', 4);
            put('e', 5);
            put('E', 5);
            put('f', 6);
            put('F', 6);
            put('g', 7);
            put('G', 7);
            put('h', 8);
            put('H', 8);
            put('i', 9);
            put('I', 9);
            put('j', 10);
            put('J', 10);
            put('k', 11);
            put('K', 11);
            put('l', 12);
            put('L', 12);
            put('m', 13);
            put('M', 13);
            put('n', 14);
            put('N', 14);
            put('o', 15);
            put('O', 15);
            put('p', 16);
            put('P', 16);
            put('q', 17);
            put('Q', 17);
            put('r', 18);
            put('R', 18);
            put('s', 19);
            put('S', 19);
            put('t', 20);
            put('T', 20);
            put('u', 21);
            put('U', 21);
            put('v', 22);
            put('V', 22);
            put('w', 23);
            put('W', 23);
            put('x', 24);
            put('X', 24);
            put('y', 25);
            put('Y', 25);
            put('z', 26);
            put('Z', 26);
        }};
        int prev = alphabetDict.get(array[0]);
        for (int i  = 1; i < array.length; i++) {
            if (prev + 1 != alphabetDict.get(array[i])) {
                System.out.println(array[i]);
            }
            prev = alphabetDict.get(array[i]);

        }
        return ' ';
    }

    public static void main(String[] args) {
        FindTheMissingLetter.findMissingLetter(new char[] {'O','Q','R','S' });
    }
}

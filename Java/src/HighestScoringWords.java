import java.util.HashMap;
import java.util.Map;

public class HighestScoringWords {
    public static String high(String s) {
        int counter = 0;
        int maxNumber = 0;
        String maxWord = "";
        String[] wordsArray = s.split(" ");
        Map<Character, Integer> alphabetDict = new HashMap<Character, Integer>() {{
            put('a', 1);
            put('b', 2);
            put('c', 3);
            put('d', 4);
            put('e', 5);
            put('f', 6);
            put('g', 7);
            put('h', 8);
            put('i', 9);
            put('j', 10);
            put('k', 11);
            put('l', 12);
            put('m', 13);
            put('n', 14);
            put('o', 15);
            put('p', 16);
            put('q', 17);
            put('r', 18);
            put('s', 19);
            put('t', 20);
            put('u', 21);
            put('v', 22);
            put('w', 23);
            put('x', 24);
            put('y', 25);
            put('z', 26);
        }};
        for (String word: wordsArray) {
            counter = 0;
            for (int i = 0; i < word.length(); i++) {
                counter += alphabetDict.get(word.charAt(i));
            }
            if (counter > maxNumber) {
                maxNumber = counter;
                maxWord = word;
            }
        }
        return maxWord;
    }
    public static void main(String[] args) {
        System.out.println(HighestScoringWords.high("man i need a taxi up to ubud"));
    }
}

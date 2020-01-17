package Poker.Main;

import java.util.*;


public class PokerHand {
    // probably best to have an array that is sorted and goes from -- to ---
    public enum Result { TIE, WIN, LOSS }
    String[] pokerHandArray = new String[5];
    Map<Character, Integer> cardToRankingDict = new HashMap<Character, Integer>() {{
        put('2', 2);
        put('3', 3);
        put('4', 4);
        put('5', 5);
        put('6', 6);
        put('7', 7);
        put('8', 8);
        put('9', 9);
        put('T', 10);
        put('J', 11);
        put('Q', 12);
        put('K', 13);
        put('A', 14);
    }};
    Map<Integer, Character> rankToCardDict = new HashMap<Integer, Character>() {{
        put(2, '2');
        put(3, '3');
        put(4, '4');
        put(5, '5');
        put(6, '6');
        put(7, '7');
        put(8, '8');
        put(9, '9');
        put(10, 'T');
        put(11, 'J');
        put(12, 'Q');
        put(13, 'K');
        put(14, 'A');
    }};
    Set<String> pokerHandSet = new HashSet<String>();
    Set<Integer> pokerCardRankSet = new HashSet<Integer>();
    public PokerHand(String hand) {
        pokerHandArray = hand.split(" ");
        for (String i: pokerHandArray) {
            pokerHandSet.add(i);
            pokerCardRankSet.add(cardToRankingDict.get(i.charAt(0))); // havent checked
        }
    } // constructor

    public int getLowestRank() {
        int lowest = Integer.MAX_VALUE;
        for (String i: pokerHandArray) {
            if (cardToRankingDict.get(i.charAt(0)) < lowest) {
                lowest = cardToRankingDict.get(i.charAt(0));
            }
        }
        return lowest;
    }

    public boolean checkCardDuplicates(int numSameRank, String card) {
        int counter = 0;
        for (String j: pokerHandArray) {
            if (j.charAt(0) == card.charAt(0)) {
                counter += 1;
            }
        }
        if (counter == numSameRank) {
            return true;
        }
        return false;

    }

    public boolean checkRoyalFlush() {
        char suit = pokerHandArray[0].charAt(1);
        if (!pokerHandSet.contains("" + 'A' + suit)) {
            return false;
        }
        if (!pokerHandSet.contains("" + 'K' + suit)) {
            return false;
        }
        if (!pokerHandSet.contains("" + 'Q' + suit)) {
            return false;
        }
        if (!pokerHandSet.contains("" + 'J' + suit)) {
            return false;
        }
        if (!pokerHandSet.contains("" + 'T' + suit)) {
            return false;
        }
        return true;
    } // 1

    public boolean checkStraightFlush() {
        char suit = pokerHandArray[0].charAt(1);
        int lowest = getLowestRank();
        for (int i = 1; i < 5; i++) {
            if (!pokerHandSet.contains("" + rankToCardDict.get(lowest + i) + suit)) {
                return false;
            }
        }
        return true;
    } // 2

    public boolean checkFourOfAKind() {
        for (int i = 0; i < 2; i++) {
            if (checkCardDuplicates(4, pokerHandArray[i])) {
                return true;
            }
        }
        return false;
    } // 3

    public boolean checkFlush() {
        char suit = pokerHandArray[0].charAt(1);
        for (int i = 1; i < 5; i++) {
            if (pokerHandArray[i].charAt(1) != suit) {
                return false;
            }
        }
        return true;
    } // 5

    public boolean checkStraight() {
        int lowest = getLowestRank();
        for (int i = 1; i < 5; i++) {
            if (!pokerCardRankSet.contains(lowest + i)) {
                return false;
            }
        }
        return true;
    } // 6

    public boolean checkThreeOfAKind() {
        for (int i = 0; i < 3; i++) {
            if (checkCardDuplicates(3, pokerHandArray[i])) {
                return true;
            }
        }
        return false;
    } // 7

    public boolean checkTwoOfAKind() {
        for (int i = 0; i < 4; i++) {
            if (checkCardDuplicates(2, pokerHandArray[i])) {
                return true;
            }
        }
        return false;
    } // 9

    public String getHighestCard() {
        int highestRank = Integer.MIN_VALUE;
        String highestCard = "";
        for (String i: pokerHandArray) {
            if (cardToRankingDict.get(i.charAt(0)) > highestRank) {
                highestRank = cardToRankingDict.get(i.charAt(0));
                highestCard = i;
            }
        }
        return highestCard;
    } // 10

}

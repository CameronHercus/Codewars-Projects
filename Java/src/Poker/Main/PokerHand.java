package Poker.Main;

import java.util.*;


public class PokerHand {
    // probably best to have an array that is sorted and goes from -- to ---
    public enum Result { TIE, WIN, LOSS }
    String[] pokerHand = new String[5];
    Integer[] handCardRankings = new Integer[5];
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
    Map<String, Integer> pokerHandDict = new HashMap<String, Integer>();
    Set<String> pokerHandSet = new HashSet<String>();
    private Character suit;
    public PokerHand(String hand) {
        pokerHand = hand.split(" ");
        for (String i: pokerHand) {
            pokerHandDict.put(i, cardToRankingDict.get(i.charAt(0)));
            pokerHandSet.add(i);
        }
    }
    //MAKE A GET CARDRANK FUNCTION

    public String[] getPokerHand() {
        return pokerHand;
    }

    public Map<String, Integer> getPokerHandDict() {
        return pokerHandDict;
    }

    public boolean checkRoyalFlush() {
        suit = pokerHand[0].charAt(1);
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
    }

    public boolean checkStraightFlush() {
        suit = pokerHand[0].charAt(1);
        int lowest = getLowestRanking();
        for (int i = 1; i < 5; i++) {
            if (!pokerHandSet.contains("" + rankToCardDict.get(lowest + i) + suit)) {
                return false;
            }
        }
        return true;
    }

    public boolean checkFlush() {
        suit = pokerHand[0].charAt(1);
        for (String i: pokerHand) {
            if (i.charAt(1) != suit) {
                return false;
            }
        }
        return true;
    }

    public int getLowestRanking() {
        int lowest = Integer.MAX_VALUE;
        for (String i: pokerHand) {
            if (pokerHandDict.get(i) < lowest) {
                lowest = pokerHandDict.get(i);
            }
        }
        return lowest;
    }

    public boolean checkStraight() {
        int lowest = getLowestRanking();
        for (int i = 1; i < 5; i++) {
            if (!pokerHandDict.containsValue(lowest + i)) {
                return false;
            }
        }
        return true;
    }

    public String getHighestCard() {
        int highestRank = Integer.MIN_VALUE;
        String highestCard = "";
        for (String i: pokerHand) {
            if (cardToRankingDict.get(i.charAt(0)) > highestRank) {
                highestRank = cardToRankingDict.get(i.charAt(0));
                highestCard = i;
            }
        }
        return highestCard;
    }

    public static void main(String[] args) {
    }

}

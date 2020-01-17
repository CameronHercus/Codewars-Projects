package Poker.Test;

import Poker.Main.PokerHand;
import org.junit.Test;

import static org.junit.Assert.*;

public class PokerHandTest {

    @Test
    public void getPokerHand() {
    }

    @Test
    public void getPokerHandDict() {
    }

    @Test
    public void checkRoyalFlush() {
        assertTrue(new PokerHand("AD KD QD JD TD").checkRoyalFlush());
        assertFalse(new PokerHand("AD KD QD JD 8D").checkRoyalFlush());
        assertFalse(new PokerHand("AD 2D 3D 4D TD").checkRoyalFlush());
        assertFalse(new PokerHand("AH 2D 3D 4D TD").checkRoyalFlush());
    }

    @Test
    public void getLowestRanking() {
    }

    @Test
    public void checkStraight() {
        assertTrue(new PokerHand("8D 7D 6D 5D 4D").checkStraight());
        assertTrue(new PokerHand("5H 6C 4S 7D 8D").checkStraight());
        assertFalse(new PokerHand("2D 7D 6D 5D 4D").checkStraight());
    }

    @Test
    public void checkStraightFlush() {
        assertTrue(new PokerHand("8D 7D 6D 5D 4D").checkStraightFlush());
        assertFalse(new PokerHand("3D 5D 6D 7D 8D").checkStraightFlush());
        assertFalse(new PokerHand("4D 5D 6D 7D 9D").checkStraightFlush());
        assertFalse(new PokerHand("TD 9D 6D 7D 4D").checkStraightFlush());
        assertTrue(new PokerHand("TD 9D 6D 7D 8D").checkStraightFlush());
        assertFalse(new PokerHand("4H 5D 6D 7D 8D").checkStraightFlush());
        assertFalse(new PokerHand("2D 7D 6D 5D 4D").checkStraightFlush());
        assertTrue(new PokerHand("3D 7D 6D 5D 4D").checkStraightFlush());
        assertFalse(new PokerHand("3D 4D 5D 6D 7H").checkStraightFlush());
        assertFalse(new PokerHand("3H 4D 5D 6D 7H").checkStraightFlush());
    }

    @Test
    public void checkFlush() {
        assertTrue(new PokerHand("TD JD 6D 5D 4D").checkFlush());
        assertTrue(new PokerHand("TH JH 6H 5H 4H").checkFlush());
        assertTrue(new PokerHand("TS JS 6S 5S 4S").checkFlush());
        assertTrue(new PokerHand("TC JC 6C 5C 4C").checkFlush());
        assertFalse(new PokerHand("TH JD 6D 5D 4D").checkFlush());
        assertFalse(new PokerHand("TH JH 6H 5H 4D").checkFlush());
        assertFalse(new PokerHand("TH JD 6S 5C 4H").checkFlush());
    }

    @Test
    public void checkFourOfAKind() {
        assertTrue(new PokerHand("9D 9C 9S 9H 4D").checkFourOfAKind());
        assertTrue(new PokerHand("9D 8C 8S 8H 8D").checkFourOfAKind());
        assertTrue(new PokerHand("JD 8C JS JH JS").checkFourOfAKind());
        assertTrue(new PokerHand("8D JD JS JH JS").checkFourOfAKind());
        assertTrue(new PokerHand("JD JS 8S JH JS").checkFourOfAKind());
        assertFalse(new PokerHand("TH JD 6D 5D 4D").checkFourOfAKind());
        assertFalse(new PokerHand("TH JH 6H 5H 4D").checkFourOfAKind());
        assertFalse(new PokerHand("TH JD 6S 5C 4H").checkFourOfAKind());
    }

    @Test
    public void checkThreeOfAKind() {
        assertTrue(new PokerHand("9D 9C 9S 8H 4D").checkThreeOfAKind());
        assertTrue(new PokerHand("8D 9C 9S 9H 4D").checkThreeOfAKind());
        assertTrue(new PokerHand("8D 7C 9S 9H 9D").checkThreeOfAKind());
        assertTrue(new PokerHand("9D 7C 8S 9H 9C").checkThreeOfAKind());
        assertTrue(new PokerHand("9D 9C 8S 7H 9H").checkThreeOfAKind());
        assertFalse(new PokerHand("9D 7C 8S 7H 9H").checkThreeOfAKind());
        assertFalse(new PokerHand("7D 7C 8S 8H 9H").checkThreeOfAKind());
        assertFalse(new PokerHand("1D 2C 3S 4H 5H").checkThreeOfAKind());
    }

    @Test
    public void checkTwoOfAKind() {
        assertTrue(new PokerHand("9D 9C 7S 8H 4D").checkTwoOfAKind());
        assertTrue(new PokerHand("3D 9C 9S 8H 4D").checkTwoOfAKind());
        assertTrue(new PokerHand("3D 5C 9S 9H 4D").checkTwoOfAKind());
        assertTrue(new PokerHand("3D 5C TS 9H 9D").checkTwoOfAKind());
        assertTrue(new PokerHand("9D 5C TS 3H 9H").checkTwoOfAKind());
        assertFalse(new PokerHand("9D 5C TS 3H 7H").checkTwoOfAKind());
    }

    @Test
    public void getHighestCard() {
    }
}
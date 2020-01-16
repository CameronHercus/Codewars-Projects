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
    }

    @Test
    public void main() {
    }

    @Test
    public void checkStraightFlush() {
        assertTrue(new PokerHand("8D 7D 6D 5D 4D").checkStraightFlush());
        assertFalse(new PokerHand("2D 7D 6D 5D 4D").checkStraightFlush());
        assertTrue(new PokerHand("3D 7D 6D 5D 4D").checkStraightFlush());
        assertFalse(new PokerHand("3D 4D 5D 6D 7H").checkStraightFlush());
        assertFalse(new PokerHand("3H 4D 5D 6D 7H").checkStraightFlush());
    }
}
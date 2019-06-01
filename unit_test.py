import unittest
import Blackjack


class BlackjackTestCases(unittest.TestCase):
    #Unit 01.1 test if length of deck is 52 
    def test_create_deck_length(self):
        deck = Blackjack.create_deck()
        self.assertEqual(len(deck), 52, "Deck length should be 52")

    #Unit 0.1.2 test if deck contains 13 Hearts
    def test_create_deck_hearts(self):
        deck = Blackjack.create_deck()
        heartsList = [i for i in deck if i.endswith("Hearts")]
        self.assertEqual(len(heartsList), 13, "HeartsList length should be 13")
        
    #Unit 0.1.3 test if deck contains 13 Clubs
    def test_create_deck_clubs(self):
        deck = Blackjack.create_deck()
        clubsList = [i for i in deck if i.endswith("Clubs")]
        self.assertEqual(len(clubsList), 13, "ClubsList length should be 13")
        
    #Unit 0.1.4 test if deck contains 13 Diamonds
    def test_create_deck_diamonds(self):
        deck = Blackjack.create_deck()
        diamondsList = [i for i in deck if i.endswith("Diamonds")]
        self.assertEqual(len(diamondsList), 13, "DiamondsList length should be 13")

    #Unit 0.1.5 test if deck contains 13 Spades
    def test_create_deck_spades(self):
        deck = Blackjack.create_deck()
        spadesList = [i for i in deck if i.endswith("Spades")]
        self.assertEqual(len(spadesList), 13, "SpadesList length should be 13")

    #Unit 0.2.1 test if deal() function removes 1 card from the deck[]
    def test_deal_function_length(self):
        Blackjack.deal()
        self.assertEqual(len(Blackjack.deck), 51, "Length of deck should be 51")     

    #Unit 0.3.1 test if card_value(card_name) function finds the correct value in the dictionary
    def test_card_value_output(self):
        card_name = 'A of Spades'
        return_value = Blackjack.card_value(card_name)
        self.assertEqual(return_value, 11, "The returned Value should be 11 ")

    #Unit 0.4.1 test if and ace returns 1 when current_value exceeds 21
    def test_check_for_ace_one(self):
        card_name = 'A of Spades'
        current_value = 15
        return_value = Blackjack.check_for_ace(card_name, current_value)
        self.assertEqual(return_value, 1, "The returned value should be 1")
    
    #Unit 0.4.2 test if an ace returns 11 when current_value is subceeds 22
    def test_check_for_ace_eleven(self):
        card_name = 'A of Spades'
        current_value = 10
        return_value = Blackjack.check_for_ace(card_name, current_value)
        self.assertEqual(return_value, 11, "The returned value should be 11")
    
    #Unit 0.4.3 test if a non-ace card returns the correct value
    def test_check_for_non_ace(self):
        card_name = 'K of Spades'
        current_value = 10
        return_value = Blackjack.check_for_ace(card_name, current_value)
        self.assertEqual(return_value, current_value, "The returned value should be 10")

    #Unit 0.5.1 test if dealer stops getting cards after hitting 17
    def test_check_if_17_stops(self):
        dealer_global_value = 17
        return_value = Blackjack.dealer_deal(dealer_global_value)
        self.assertEqual(return_value, dealer_global_value, "return_value should be 17")

    #Unit 0.5.2 test if dealer draws after not having a value of 15
    def test_check_if_15_draws(self):
        Blackjack.create_deck()
        dealer_global_value = 15
        return_value = Blackjack.dealer_deal(dealer_global_value)
        self.assertGreater(return_value, dealer_global_value, "return_value should be greater than than 15")

if __name__ == "__main__":
    unittest.main()
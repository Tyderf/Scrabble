from unittest import TestCase
import Scrabble


class TestScrabble(TestCase):
    def setUp(self):
        self.scrabble_ = Scrabble.Scrabble("boatruneatforghadwest")

    def test_update_hand(self):
        s = Scrabble
        # badefdd
        # fad
        # bded
        # Check to make sure that the letters in the word, are not in the hand
        # Have correct length
        testWord = "fad"
        testHand = "bfrsadefd"
        expectedResult = "brsefd"
        update_hand = self.scrabble_.update_hand(testHand, testWord)
        result = (update_hand == expectedResult)

        if not result:
            self.fail()

    # def test_is_valid_word(self):
    #     wordThatPasses = "boat"
    #     notInWordList = "whatfor"
    #     notInHand = "and"
    #     testHand = "boatagn"
    #     wordList = ["boat", "eat"]
    #     s = Scrabble
    #     validWord = self.scrabble_.is_valid_word(wordThatPasses, testHand, wordList)
    #
    #     if not validWord:
    #         self.fail()
    #
    #     invalidWord = self.scrabble_.is_valid_word(notInWordList, testHand, wordList)
    #
    #     if invalidWord:
    #         self.fail()
    #
    #     invalidHand = self.scrabble_.is_valid_word(notInHand, testHand, wordList)
    #
    #     if invalidHand:
    #         self.fail()
    #
    # def test_get_word_score(self):
    #     # Given a word and a number, return the correct score
    #     word = "test"
    #     number = 7
    #     s = Scrabble
    #     wordScore = self.scrabble_.get_word_score(word, number)
    #     expected_number = 16
    #     result = (wordScore == expected_number)
    #
    # def test_deal_hand_new(self):
    #     #
    #     lettersInHand = "boatruneatforghadwest"
    #     hand = lettersInHand
    #     s = Scrabble
    #     test_word_list = ["boat", "run", "eat"]
    #     new_hand_option = "new"
    #     old_test_hand = self.scrabble_.deal_hand(lettersInHand)
    #     self.scrabble_.display_hand(hand)
    #     new_hand = self.scrabble_.play_hand(lettersInHand, test_word_list, new_hand_option)
    #     if new_hand == old_test_hand:
    #         self.fail()

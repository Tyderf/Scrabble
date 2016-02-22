# 6.00 Problem Set 3A Solutions
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
#

import random
import time
import sys
import math
import collections

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


class Scrabble:
    hand_options = ["n", "r", "e"]
    hand_size = 7


    def load_words(self):

        """
        Returns a list of valid words. Words are strings of lowercase letters.

        Depending on the size of the word list, this function may
        take a while to finish.
        """
        print("Loading word list from file...")
        # inFile: file
        inFile = open(WORDLIST_FILENAME, 'r')
        # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.append(line.strip().lower())
        print("  ", len(wordlist), "words loaded.")
        return wordlist

    def get_frequency_dict(self, sequence):
        """
        Returns a dictionary where the keys are elements of the sequence
        and the values are integer counts, for the number of times that
        an element is repeated in the sequence.

        sequence: string or list
        return: dictionary
        """
        # freqs: dictionary (element_type -> int)
        freq = {}
        for x in sequence:
            freq[x] = freq.get(x, 0) + 1
        return freq

    # (end of helper code)
    # -----------------------------------

    #
    # Problem #1: Scoring a word
    #
    def get_word_score(self, word, number):

        """
        ^^^^^
        |||||
        implement this
        Word
        First, run the test to make sure it failed
        Then, you need to write code in the get_word_score function
        until the test passes

        Returns the score for a word. Assumes the word is a
        valid word.

        The score for a word is the sum of the points for letters
        in the word multiplied by the length of the word, plus 50
        points if all n letters are used on the first go.

        Letters are scored as in Scrabble; A is worth 1, B is
        worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

        word: string (lowercase letters)
        returns: int >= 0
        abac
        """

        score = 0
        for letter in word:
            score += SCRABBLE_LETTER_VALUES[letter]
        # TO DO...
        totalScore = score * len(word)
        if len(word) == number:
            totalScore += 50
        return totalScore

    #
    # Make sure you understand how this function works and what it does!
    #
    def display_hand(self, hand):
        """
        Displays the letters currently in the hand.

        For example:
           display_hand({'a':1, 'x':2, 'l':3, 'e':1})
        Should print out something like:
           a x x l l l e
        The order of the letters is unimportant.

        hand: dictionary (string -> int)
        """
        for letter in list(hand.keys()):
            for j in range(hand[letter]):
                print(letter, end='')  # print all on the same line
        print()  # print an empty line

    #
    # Make sure you understand how this function works and what it does!
    #
    def deal_hand(self, letters_in_hand):
        """
        Returns a random hand containing n lowercase letters.
        At least n/3 the letters in the hand should be VOWELS.

        Hands are represented as dictionaries. The keys are
        letters and the values are the number of times the
        particular letter is repeated in that hand.

        n: int >= 0
        returns: dictionary (string -> int)
        """

        hand = {}
        letters_in_hand = 6
        num_vowels = letters_in_hand / 3

        for i in range(int(num_vowels)):
            x = VOWELS[random.randrange(0, len(VOWELS))]
            hand[x] = hand.get(x, 0) + 1

        for i in range(int(num_vowels), letters_in_hand):
            x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
            hand[x] = hand.get(x, 0) + 1

        return hand

    #
    # Problem #2: Update a hand by removing letters
    #
    def update_hand(self, hand, word):
        # remove letters in word from letters in hand
        # for each letter in the word
        for letter in word:
            # check to see if the letter is in word\
            if letter in hand:
                # if it is then remove the letter
                # hand = str(hand)
                del hand[letter]
        return hand
        # if it isn't then leave it




        """
        Assumes that 'hand' has all the letters in word.
        In other words, this assumes that however many times
        a letter appears in 'word', 'hand' has at least as
        many of that letter in it.

        Updates the hand: uses up the letters in the given word
        and returns the new hand, without those letters in it.

        Has no side effects: does not modify hand.

        word: string
        hand: dictionary (string -> int)
        returns: dictionary (string -> int)
        """
        # TO DO ...

    #
    # Problem #3: Test word validity
    #
    def is_valid_word(self, word_choice, hand, word_list):
        # check if word is in wordlist
        word = word_choice
        # Are the letters in the hand, in the word
        # For each duplicate letter (as in the letter "t" in the word "letter")
        # Make sure each instance of the letter matches an instance in the hand

        if word in word_list and word in hand and len(word) != 1 or word == 'a':
            # return true
            return True
        else:
            return False

    def is_valid_word_choice(self, word_choice, hand, word_list):
        # Check if the word choice the user entered is valid
        if word_choice in word_list and hand:
            return True

        """
        Returns True if word is in the word_list and is entirely
        composed of letters in the hand. Otherwise, returns False.
        Does not mutate hand or word_list.

        word: string
        hand: dictionary (string -> int)
        word_list: list of lowercase strings
        """
        # TO DO...

    def calculate_handlen(self, hand):
        handlen = 0
        for v in hand.values():
            handlen += v
        return handlen

    #
    # Problem #4: Playing a hand
    #
    def convert_alphabet_dict_to_str(self, scrabble_letter_values_ordered):
        alphabet = ''
        for letter in list(scrabble_letter_values_ordered.keys()):
            alphabet += letter

        def get_alphabet():
            return alphabet
        return get_alphabet


    def play_hand(self, hand, word_list, letters_in_hand):
        word_choice = None
        # While there are letters left in the hand, and the user has not opted to exit
        overall_score = 0
        if len(hand) > 0:
            while word_choice != '.':
                print("Hand: ", end="")
                # Display the hand
                print(''.join(hand))
                # Get the user's word choice
                word_choice = self.get_word(hand, word_choice, word_list)
                # Get the word score for the word choice
                score = self.get_word_score(word_choice, self.hand_size)
                # Update the hand, removing the letters of the word choice from the letters of the hand
                hand = self.update_hand(hand, word_choice)
                print("Score: ", score)
                overall_score += score
                print("Over all game score: ", overall_score)
                print('')
            else:
                hand = self.deal_hand(letters_in_hand)
                self.play_hand(hand, word_list, letters_in_hand)

        """
        Allows the user to play the given hand, as follows:

        * The hand is displayed.

        * The user may input a word.

        * An invalid word is rejected, and a message is displayed asking
          the user to choose another word.

        * When a valid word is entered, it uses up letters from the hand.

        * After every valid word: the score for that word is displayed,
          the remaining letters in the hand are displayed, and the user
          is asked to input another word.

        * The sum of the word scores is displayed when the hand finishes.

        * The hand finishes when there are no more unused letters.
          The user can also finish playing the hand by inputting a single
          period (the string '.') instead of a word.

          hand: dictionary (string -> int)
          word_list: list of lowercase strings

        """
        # TO DO ...

    def get_word(self, hand, letters_in_hand, word_list):
        exit_hand = '.'
        word_choice = input("Please choose a word: ")
        if exit_hand == word_choice:
            print(" Ending Hand...")
            print('')
            print('')
            # time.sleep(500)
            self.play_game(hand, word_list, letters_in_hand)
        is_valid_word = self.is_valid_word(word_choice, hand, word_list)
        # is_valid_word_choice = self.is_valid_word_choice(word_choice, hand, word_list)
        while is_valid_word is False:
            print("Please choose a word that is valid", "\n")
            word_choice = self.get_word(hand, letters_in_hand, word_list)
            is_valid_word = True

        return word_choice

    #
    # Problem #5: Playing a game
    # Make sure you understand how this code works!
    #
    def play_game(self, hand, word_list, letters_in_hand):
        hand_to_play = ['n', 'r', 'e']
        exit_game = 'e'
        new_hand = 'n'
        while hand_to_play not in self.hand_options:
            print(" SCRABBLE", '\n', "---------")
            print(" n for a new random hand", '\n', "r to play the last hand again", '\n', "e to exit the game")
            hand_to_play = input(" What hand do you want to play?: ")
        if hand_to_play == exit_game:
            print(" Exiting game...")
            time.sleep(1000)
            sys.exit(0)
        elif hand_to_play == new_hand:
            hand = self.deal_hand(letters_in_hand)
            self.play_hand(hand, word_list, letters_in_hand)
        else:
            self.play_hand(hand, word_list, letters_in_hand)
        """
        Allow the user to play an arbitrary number of hands.

        * Asks the user to input 'n' or 'r' or 'e'.

        * If the user inputs 'n', let the user play a new (random) hand.
          When done playing the hand, ask the 'n' or 'e' question again.

        * If the user inputs 'r', let the user play the last hand again.

        * If the user inputs 'e', exit the game.

        * If the user inputs anything else, ask them again.
        """
        # TO DO...

    #
    # Build data structures used for entire session and play game
    #
    def __init__(self, letters_in_hand):
        hand = self.deal_hand(letters_in_hand)
        word_list = self.load_words()
        self.play_game(hand, word_list, letters_in_hand)

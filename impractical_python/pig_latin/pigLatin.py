"""Pig latin sentence generator"""

import sys


def goodbye():
    print("eesay ouyay aterlay!")
    sys.exit()


def pigify(sentence):
    vowels = ("a", "e", "i", "o", "u")

    piggy = []

    for word in sentence.lower().split():
        if word[0] not in vowels:
            word = word[1::] + word[0] + "ay"
        else:
            word += "way"
        piggy.append(word)
    return "\n" + " ".join(piggy) + "\n"


def user_input():
    while True:
        user_words = input("Enter a sentence or enter q to quit: \n> ")
        if user_words == "q":
            goodbye()
        print(pigify(user_words))


if __name__ == "__main__":
    user_input()

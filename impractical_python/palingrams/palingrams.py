import load_dictionary
import time

start = time.time()

word_list = load_dictionary.load('dictionary.txt')

words = set(word_list)

palindromes = [word for word in word_list if len(word) > 1 and word == word[::-1]]


def find_palingram():
    pali_word = []
    for word in words:
        end, rev_word = len(word), word[::-1]
        if end > 1:
            for i in range(end):
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in words:
                    pali_word.append((word, rev_word[end-i:]))
    return pali_word


# print(f"Number of palindromes found:{len(palindromes)}")
# splat (asterisk) operator unpacks items in object, sep is used to specify how we want the items to be seperated by
# print(*palindromes, sep="\n")

palingrams = find_palingram()

# print(sorted(palingrams))

end = time.time()

# print(f"total run time {end - start} ")

def is_palingram(str):
    new_string, i = "", 0
    while i < len(str):
        if str[i].lower().isalpha():
            new_string += str[i]
        i += 1
    return new_string == new_string[::-1]


def is_palindrome(str):
    if len(str) <= 1:
        return True
    return str[0] == str[-1] and is_palindrome(str[1:-1])








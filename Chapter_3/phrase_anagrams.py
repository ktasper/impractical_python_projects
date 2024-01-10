import load_dict
from collections import Counter

def main():
    word_list = load_dict.load('words.txt')
    # ensure "a" & "I" (both lowercase) are included
    word_list.append('a')
    word_list.append('i')
    word_list = set(word_list)
    word_list = sorted(word_list)
    input_name = input("Input name: ")

    # Phrase Length and Name Length Counters
    name_len = len(input_name)
    phrase_len = 0

    print (find_anagrams(input_name, word_list))


def find_anagrams(name: str, word_list: list) -> list:
    """Read name & dictionary file & display all anagrams IN name."""
    # Counter uses a dictionary structure with the letter as the key and the count as the value.
    name_letter_map = Counter(name)
    anagrams = []
    for word in word_list:
        test = ''
        word_letter_map = Counter(word.lower())
        for char in word:
            if word_letter_map[char] <= name_letter_map[char]:
                test += char
        if Counter(test) == word_letter_map:
            anagrams.append(word)
    return anagrams


if __name__ == '__main__':
    main()


# Processing the User’s Choice
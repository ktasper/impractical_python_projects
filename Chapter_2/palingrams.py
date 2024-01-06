"""
Objective: Use Python to search an English language dictionary for two-word palingrams. Analyze
and optimize the palingram code using the cProfile tool.
"""
from load_dict import load


def main():
    palngrams = find_palingrams('./words.txt')
    pali_sorted = sorted(palngrams)

    print("\nNumber of palingrams = {}\n".format(len(pali_sorted)))
    for first, second in pali_sorted:
        print("{} {}".format(first, second))


def find_palingrams(word_file: str) -> list[str]:
    """
    Given a list of words returns a list of palingrams
    """
    pali_list: list = []
    word_list = load(word_file)

    for word in word_list:
        word = word.strip('\n')

        end = len(word)
        rev_word = word[::-1]

        if len(word) > 1:
        # Loop over the letters in the word
            for i in range(end):
                # Now, run a conditional requiring the back end of the word to be palindromic 
                # and the front end to be a reverse word in the word list (in other words, a “real” word)
                if word[i:] == rev_word[:end - i] and rev_word[end - i:] in word_list:
                    pali_list.append((word, rev_word[end-i:]))
                # have to repeat the conditional, but change the slicing direction 
                # and word order to reverse the output. In other words, you must capture palindromic sequences
                # at the start of the word rather than at the end
                if word[:i] == rev_word[end - i:] and rev_word[:end - i] in word_list:
                    pali_list.append((rev_word[:end-i], word))
    return pali_list

if __name__ == "__main__":
    main()

"""Find palindromes (letter palingrams) in a dictionary file."""
import load_dict


word_list = load_dict.load('words.txt')
pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

# Splat operator instead of for loop
print (*pali_list, sep='\n')
print (f'Number of palindromes: {len(pali_list)}')

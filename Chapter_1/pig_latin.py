"""
Takes a word as input and returns the pig latin
you take an English word that begins with a consonant,
move that consonant to the end, and then add “ay” to the end of the word.
If the word begins with a vowel, you simply add “way” to the end of the
word
"""

vowels = ('a','e','i','o','u')
input_word = input("Give me your word: ")

if input_word[0] in vowels:
    print(f'{input_word}way')
else:
    # Move the first consonant to the end and add ay
    first_char = input_word[0]
    print (f'{input_word[1:]}{first_char}ay')

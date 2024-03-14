"""
The six most commonly used letters in the English language can be remembered with the mnemonic “etaoin” (pronounced eh-tay-oh-in). Write a Python 
script that takes a sentence (string) as input and returns a simple bar chart–
type display as in Figure 1-2. Hint: I used a dictionary data structure and two 
modules that I haven’t covered yet, pprint and collections/defaultdict.
"""

from collections import defaultdict
import pprint


input_text = "This is a test string to see if this works"
# Create a default dict to prevent key errors when inserting data
dd_dict = defaultdict(list)

for word in input_text.split():
    for char in word:
        dd_dict[char].append(char)

pprint.pprint (dd_dict)

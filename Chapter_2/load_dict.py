"""Load a text file as a list.
Arguments:
-text file name (and directory path, if needed)
Returns:
-A list of all words in a text file in lower case.
Requires-import sys
"""

def load(file):
    """Open a text file and return a list of lowercase strings"""
    with open(file, encoding='utf-8') as f:
        loaded_txt = f.read().strip().split('\n')
        loaded_txt = [x.lower() for x in loaded_txt]
        return loaded_txt

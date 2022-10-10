import unicodedata
from typing import List


def strip_accents(word: str) -> str:
    return ''.join(
        letter
        for letter in unicodedata.normalize('NFD', word)
        if unicodedata.category(letter) != 'Mn'
    )


def read_words() -> List[str]:
    with open('data.txt', 'r', encoding='utf-8') as f:
        words: List[str] = [
            strip_accents(line.strip('\n'))
            for line in f
        ]

    return words


HANGMAN_PICS: List[str] = [
    '''
''',
    '''
  +---+
  |   |
      |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''',
    '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
]

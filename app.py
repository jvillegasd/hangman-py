import os
import random
from typing import List

import loader


def select_word(words: List[str]) -> str:
    return random.choice(words)


def update_word_label(input_letter: str, word: str, word_label: str) -> str:
    word_label_list: List[str] = list(word_label)
    for i, letter in enumerate(word):
        if letter == input_letter:
            word_label_list[i * 2] = letter

    return ''.join(word_label_list)


def run():
    words: List[str] = loader.read_words()

    while True:
        fails: int = 0
        guested_letters: int = 0
        word: str = select_word(words)
        word_status: str = word
        word_label: str = '_ ' * len(word)

        while guested_letters < len(word):
            os.system('clear')
            hangman_pic: str = loader.HANGMAN_PICS[fails]

            print('Hangman', 'Created by Jvillegasd')
            print(hangman_pic)
            print(f'word: {word_label}')

            input_letter: str = input('Type a letter and press enter: ')
            if input_letter in word_status:
                guested_letters += word_status.count(input_letter)
                word_label = update_word_label(
                    input_letter,
                    word_status,
                    word_label
                )
                word_status = word_status.replace(input_letter, ' ')
            else:
                fails += 1

            if fails >= len(loader.HANGMAN_PICS):
                break

        print('\n')
        if guested_letters == len(word):
            print('You win!', '\n')
        else:
            print(f'You lose, the word was "{word}"', '\n')

        response: str = input('Press "Y" for continue... ')
        if response != 'Y':
            break


if __name__ == '__main__':
    run()

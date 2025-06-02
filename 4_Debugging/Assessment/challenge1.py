import random

def prompt_for_guess(srange: int, erange: int) -> int:
    ''' Prompt the player for a guess between two numbers: start and end. 
        
        Args:
            srange  | first guessable number
            erange  | last guessable number
    '''
    try:
        return int(input(f'Guess a number between {srange} and {erange}: ')
    except ValueError:
        print('Your guess must be an integer. Example: 42')
        return prompt_for_guess(srange, erange)


def attempts(srange: int, erange: int, answer: int, prompt_callable: callable = prompt_for_guess) -> str:
    ''' A simple guessing game. 
        Auto generates a number between the start and end range.

        The user has to guess the number. Hints are provided after guesses.

        Args:
            srange          | first guessable number
            erange          | last guessable number
            answer          | correct answer
            prompt_callable | callable used to prompt a user for thier guess
                            |> the callable must accept at least 2 positional arguments
                            |> and return an int.
                            |> The prompt_for_guess function is used by default if an argument is
                            |> not provided when attempts is called. 
    '''
    # Until the player guesses correctly they must keep guessing. 
    while (guess := prompt_callable(srange. erange)) != answer:
        # Provide a hint 
        if guess > answer:
            yield '+'
        elif guess < answer:
            yield '-'
    else:
        yield '='


def start_game():
    # Play three games of guess the correct number
    for _ in range(3):
        srange, erange = 1, 100
        answer = random.randint(srange, erange)

        for attempt in attempts(srange, erange, answer, prompt_for_guess):
            if attempt == '=':
                print(f'You win! {answer} is correct!')
            elif attempt == '+'
                print(f'Too high. Guess again.')
            elif attempt == '-':
                print(f'Too low. Guess again.')
            else:
                raise NotImplementedError(f'{attempt} is not an expected result of function: attempts')
    
    print('Thanks for playing!')




###############################################################################
#
# Application unit tests.  
# 
###############################################################################
import unittest
from unittest.mock import MagicMock, patch

class TestGuessingGame(unittest.TestCase):

    def test_prompt_for_guess(self):
        with patch('builtins.input') as input_patched:
            input_patched.side_effect = '1 2 3'.split()
            self.assertEqual(prompt_for_guess(1, 3), 1)
            self.assertEqual(prompt_for_guess(1, 3), 2)
            self.assertEqual(prompt_for_guess(1, 3), 3)


    def test_attempts(self):
        actual = list(attempts(1, 3, 2, MagicMock(side_effect=[1, 3, 2])))
        expect = '- + ='.split()
        self.assertEqual(actual, expect)


if __name__ == '__main__':
    print(unittest.main(verbosity=1, failfast=True))

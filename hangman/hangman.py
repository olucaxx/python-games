from random import choice
from typing import Tuple

def select_random_word() -> str:
    """seleciona uma palavra aleatória do arquivo words.txt e retorna ela"""
    with open('hangman/words.txt') as file:
        words = file.readlines()
        
    return choice(words).strip()


def display_list(char_list: list) -> None:
    """imprime todos os caracteres de uma lista separados por espaços no console"""
    for char in char_list:
        print(char, end=" ")
    print()
    
    
def display_lives(guesses: int) -> None:
    """imprime a quantidade de vidas restantes no console"""
    print(f"you have {guesses} guesses left!")
    

def compare_guess_with_hint(secret_word: str, hint: str, guess: str) -> bool:
    """compara o chute com a palavra secreta, atualizando as letras acertadas"""
    correct_guess = False
    for i in range(len(secret_word)):
        if secret_word[i] == guess:
            hint[i] = guess
            correct_guess = True
    return correct_guess


def validate_guess(guess: str, hint: list, secret_word: str, guessed_letters: set) -> Tuple[bool, bool]:
    """verifica o chute do usuário"""
    if len(guess) > 1:
        if len(guess) != len(secret_word):   
            return False, False
        if secret_word == guess:
            hint[:] = list(secret_word)
            return True, True
        return False, False

    if guess not in guessed_letters:
        guessed_letters.add(guess)
        correct_guess = compare_guess_with_hint(secret_word, hint, guess)
        return correct_guess, hint == list(secret_word)
    
    print("you already guessed this letter! try again.")
    return True, False


def main():
    """executa o código principal para o jogo"""
    secret_word = select_random_word()
    hint = ["_" for x in secret_word]
    guessed_letters = set()
    
    has_won = False
    guesses = 3

    while not has_won and guesses > 0:
        display_lives(guesses)
        display_list(hint)
        guess = input("what is your guess? ").lower()
        correct_guess, has_won = validate_guess(guess, hint, secret_word, guessed_letters)
        if not correct_guess:
            guesses -= 1
            
    if not has_won:
        print("you lost, better luck next time")
        print(f"the word was \"{secret_word}\"")
        exit()
    
    display_list(secret_word)
    print(f"congrats! you won!")
        
        
if __name__ == "__main__":
    main()
# Step 5
from hangman_art import logo
from hangman_words import word_list
import random

# TODO-1: - Обновите список слов, чтобы использовать 'word_list' из hangman_words.py
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# # импорт слов / import hangman_words

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# TODO-3: - Импортировать логотип из hangman_art.py и распечатайте его в начале игры.
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(logo)

# Тестирующий код / Testing code
# print(f"Pssst, the solution is {chosen_word}.")

# Создание пробелов / Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    # TODO-4: - Если пользователь ввел букву, которую он уже угадал, распечатайте букву и сообщите им об этом.
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You have already guessed this letter {guess}")

    # Проверьте угаданную букву / Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(
        # f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Проверьте, не ошибается ли пользователь. / Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - Если буквы нет в выбранном_слове, распечатайте букву и дайте им знать, что ее нет в мире.
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You have guessed wrong letter {guess}. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"Pssst, the solution is {chosen_word}.")

    # Соедините все элементы в списке и превратите его в строку.
    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Проверьте, получил ли пользователь все буквы.
    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Импортируйте этапы из hangman_art.py и устраните эту ошибку.
    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])



































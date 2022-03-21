# Step 1
import random

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
# TODO-1 - Случайным образом выберите слово из списка word_list и присвоите его переменной с именем chosen_word.
chosen_word = random.choice(word_list)

# TODO-2 - Попросите пользователя угадать букву и присвоить свой ответ переменной с именем guess.Сделайте предположение строчным.
# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess the letter:").lower()


# TODO-3 - Проверьте, является ли буква, которую пользователь угадал (угадал), одной из букв в выбранном_слове.
# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in chosen_word:
    if guess == letter:
        print("Correct!")
    else:
        print("Wrong!")

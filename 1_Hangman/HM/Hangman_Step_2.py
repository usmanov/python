# Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

# TODO-1: - Создайте пустой список с именем display.
# Для каждой буквы в выбранном_слове добавьте "_" в список "отображать".
# Итак, если выбранным словом было "apple", отображение должно быть ["_", "_", "_", "_", "_"] с 5 "_", представляющими каждую букву, которую нужно угадать.
# TODO-1: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to list 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display.append("_")

guess = input("Guess a letter: ").lower()


# TODO-2 - Перебирать каждую позицию в выбранном_слове;
# Если буква в этой позиции соответствует "угадай", то покажите эту букву на дисплее в этой позиции.
# например, если пользователь угадал "p" и выбранное слово было "apple", то отображение должно быть ["_", "p", "p", "_", "_"].
# TODO-2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter



# TODO - Выведите "display", и вы увидите угаданную букву в правильном положении, а все остальные буквы замените на "_".
# Подсказка - не беспокойтесь о том, чтобы заставить пользователя угадать следующую букву. Мы займемся этим на шаге 3.
# TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
print(display)



# TODO-3: Asking the questions
#  checking if the answer was correct
#  checking if we're in the and of quiz
#  Create class QuizBrain with __init__ method with two attributes question_number make it equal to zero,
#  and question_list to an input

# TODO-3: ЧТО НУЖНО СДЕЛАТЬ-3: Задавать вопросы
#  проверка правильности ответа
#  проверяем, подошли ли мы к концу теста
#  Создайте класс Question Brain с помощью метода __init__ с двумя атрибутами question_number,
#  сделайте его равным нулю, и question_list для ввода


    # TODO-4: Create a method next_question to retrieve an item at the current question_number from question_list.
    #  Use imput() function to show the user the Question text ans ask for user's answer.

    #  TODO-4: ЧТО НУЖНО СДЕЛАТЬ-4: Создайте метод next_question для извлечения элемента с текущим номером question_number
    #   из question_list. Используйте функцию input(), чтобы показать пользователю текст вопроса
    #   и запросить ответ пользователя.


    # TODO-5: Create a  method called still_has_questions().
    #  Return boolean depending on the value of question_number value.
    #  In the main.py use while loop to show the next question until the end.

    # TODO-5:ЧТО НУЖНО СДЕЛАТЬ - 5: Создайте метод с именем still_has_questions().
    #  Возвращает логическое значение в зависимости от значения question_number value.
    #  В main.py используйте цикл while, чтобы показать следующий вопрос до конца.

# TODO-6: Откомментируйте метод check_answer
class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1 # self.question_number = self.question_number + 1
        user_answer = input(f"В.{self.question_number}: {current_question.text} (Правда/Ложь): ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Вы все правильно поняли!")
        else:
            print("Что случилось?")
        print(f"Правильный ответ был: {correct_answer}.")
        print(f"Ваш текущий счет равен: {self.score}/{len(self.question_list) - self.question_number}")
        print("\n")


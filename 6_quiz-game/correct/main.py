from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# TODO-2: Write a for loop to iterate over the question_data.
#  Create a Question object from each entry in question_data.
#  Append each Question object to the question_bank

# TODO-2: ЧТО НУЖНО СДЕЛАТЬ-2: Напишите цикл for для перебора question_data.
#  Создайте объект Question из каждой записи в question_data.
#  Создать переменную question_text с текстом вопроса,
#  и question_answer  с текстом ответа. Создать переменную new_question для созхранения текста и ответа на вопрос.
#  Добавить каждый объект Question в question_bank.


question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Вы выполнили задание!!")
print(f"Кол-во очков: {quiz.score}/{quiz.question_number}")
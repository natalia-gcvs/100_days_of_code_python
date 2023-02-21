from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizzInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
interface = QuizzInterface(quiz)

print(question_text)
print(new_question)
print(question_bank)
from question_model import Question
from quiz_brain import QuizBrain
import requests as req
from ui import QuizInterface

params={"amount": 10, "type": "boolean"}
res = req.get("https://opentdb.com/api.php", params=params)
question_list = res.json()["results"]

question_bank = []

for question in question_list:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_interface = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

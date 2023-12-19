from questions import question_data
from question_class import Question
from quiz_QuizBrain import QuizBrain



question_bank = []
for index in question_data:
    question_text = index["text"]
    question_answer = index["answer"]
    question_object = Question(ques_ans=question_answer,ques_txt=question_text)
    question_bank.append(question_object)

q = QuizBrain(questions=question_bank)
q.playGame()
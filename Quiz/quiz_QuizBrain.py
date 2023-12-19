class QuizBrain:
    def __init__(self,questions):
        self.qeustion_number = 0
        self.question__bank = questions
        self.score = 0
        self.maxScore = len(self.question__bank)
    def nextQuestion(self):
        self.qeustion_number += 1
    def askQuestion(self):
        print(f"Question {self.qeustion_number+1} : {self.question__bank[self.qeustion_number].text}")
        self.answer = input("Answer (True/False) : ")
    def checkAnswer(self):
        if self.score == self.maxScore:
            print(f"You won.")
        if self.question__bank[self.qeustion_number].answer == self.answer:
            self.nextQuestion()
            self.score += 1
            print(f"Current score : {self.score}/{self.score}")
            return True
        else:
            return False
    def playGame(self):
        self.play = True
        while self.play:
            self.askQuestion()
            if not self.checkAnswer():
                print(f"Your lose. The correct answer was '{self.question__bank[self.qeustion_number].answer}'\nYour score : {self.score}/{self.score + 1}")
                self.play = False
    
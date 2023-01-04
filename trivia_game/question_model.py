class Question:
    def __init__(self, q_text, q_answer, incorrect_answer, question_type):
        self.text = q_text
        self.answer = q_answer
        self.incorrect_answer = incorrect_answer
        self.question_type = question_type

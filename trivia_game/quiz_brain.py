import html
import random


class QuizBrain:
    def __init__(self, q_list):
        self.ls_for_user = []
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1

        # convert html to readble text and shuffle it
        q_text = html.unescape(self.current_question.text)
        self.ls_for_user = self.clear_the_strings(
            self.current_question.incorrect_answer
        )
        self.ls_for_user.append(self.current_question.answer)
        random.shuffle(self.ls_for_user)
        return f"Q.{self.question_number}: {q_text}: "

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        return user_answer.lower() == correct_answer.lower()

    def get_type(self):
        return self.current_question.question_type

    def clear_the_strings(self, ls):
        new_ls = []
        for x in ls:
            temp = html.unescape(x)
            new_ls.append(temp)
        return new_ls

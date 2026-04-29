from datetime import datetime
import random

class Question:
    def __init__(self, question_id, text, qtype, options, correct_answer, marks, difficulty):
        self.question_id = question_id
        self.text = text
        self.qtype = qtype 
        self.options = options
        self.correct_answer = correct_answer
        self.marks = marks
        self.difficulty = difficulty

    def is_objective(self):
        return self.qtype in ["MCQ", "TF"]

    def validate(self, answer):
        return answer == self.correct_answer


class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    # ✅ FIX ADDED
    def random_select(self, n):
        return random.sample(self.questions, min(n, len(self.questions)))


class Exam:
    def __init__(self, exam_id, title, subject, duration, total_marks):
        self.exam_id = exam_id
        self.title = title
        self.subject = subject
        self.duration = duration 
        self.total_marks = total_marks
        self.questions = []
        self.status = "DRAFT"

    def add_questions(self, questions):
        self.questions.extend(questions)

    def publish(self):
        self.status = "PUBLISHED"

    def start(self):
        self.status = "ONGOING"

    def end(self):
        self.status = "COMPLETED"


class ExamAttempt:
    def __init__(self, attempt_id, student_id, exam):
        self.attempt_id = attempt_id
        self.student_id = student_id
        self.exam = exam
        self.start_time = datetime.now()
        self.end_time = None
        self.answers = {}
        self.score = 0
        self.status = "IN_PROGRESS"

    def submit_answer(self, question_id, answer):
        self.answers[question_id] = answer

    def auto_grade(self):
        score = 0
        for q in self.exam.questions:
            if q.is_objective():
                if q.question_id in self.answers and q.validate(self.answers[q.question_id]):
                    score += q.marks
        self.score = score

    def submit(self):
        self.end_time = datetime.now()
        self.status = "SUBMITTED"
        self.auto_grade()

    def auto_submit(self):
        print("Auto submitting due to timeout...")
        self.submit()


class Student:
    def __init__(self, student_id, name, roll_no):
        self.student_id = student_id
        self.name = name
        self.roll_no = roll_no
        self.attempts = []

    def start_exam(self, exam):
        attempt = ExamAttempt(len(self.attempts) + 1, self.student_id, exam)
        self.attempts.append(attempt)
        return attempt

    def view_result(self, attempt):
        return attempt.score


class Result:
    def __init__(self, attempt):
        self.attempt = attempt
        self.total_marks = sum(q.marks for q in attempt.exam.questions)
        self.scored_marks = attempt.score
        
        # ✅ safety (avoid division by zero)
        self.percentage = (self.scored_marks / self.total_marks) * 100 if self.total_marks > 0 else 0
        
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        p = self.percentage
        if p >= 90:
            return "O"
        elif p >= 80:
            return "A+"
        elif p >= 70:
            return "A"
        elif p >= 60:
            return "B+"
        elif p >= 50:
            return "B"
        elif p >= 40:
            return "C"
        else:
            return "F"

    def generate(self):
        return {
            "score": self.scored_marks,
            "percentage": self.percentage,
            "grade": self.grade
        }


# ------------------ TEST ------------------

qb = QuestionBank()
qb.add_question(Question(1, "2+2?", "MCQ", ["2", "4", "6"], "4", 5, "easy"))
qb.add_question(Question(2, "Earth is round?", "TF", ["True", "False"], "True", 5, "easy"))
qb.add_question(Question(3, "Explain gravity", "DESC", None, None, 10, "medium"))

exam = Exam(101, "Math Test", "Math", 30, 20)
exam.add_questions(qb.random_select(3))  # ✅ now works
exam.publish()

student = Student(1, "Arun", "101A")
attempt = student.start_exam(exam)

attempt.submit_answer(1, "4")
attempt.submit_answer(2, "True")

attempt.submit()

result = Result(attempt)
print(result.generate())
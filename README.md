****📝 Online Exam System (Python)****

📌 Problem Statement
Design and implement an Online Exam System that allows:

1.Creating and managing questions

2.Conducting exams for students

3.Auto-evaluating objective questions (MCQ, True/False)

4.Generating results with score, percentage, and grade
_____________________________________________________________________________

**⚙️ Approach / Logic Used**
**1. Object-Oriented Design**

The system is built using classes:

1.Question → stores question details and validation logic

2.QuestionBank → manages all questions

3.Exam → holds exam details and selected questions

4.ExamAttempt → tracks student answers and handles grading

5.Student → represents a user attempting the exam

6.Result → calculates percentage and assigns grade

_____________________________________________________________________________

**2. Key Logic**

**Question Selection**

Random questions are selected using:

random.sample()

**Answer Validation**

Only objective questions (MCQ, TF) are auto-graded

**Auto Grading**

Each correct answer adds marks to total score

**Result Calculation**

Percentage = (Scored Marks / Total Marks) × 100

_____________________________________________________________________________

**3. Workflow**

1.Add questions to Question Bank

2.Create an Exam and assign questions

3.Student starts the exam

4.Student submits answers

5.System auto-grades objective questions

6.Result is generated

_____________________________________________________________________________

**▶️ Steps to Execute the Code**

**1. Prerequisites**

Install Python (version 3.x)

**2. Run the Program**

python your_file_name.py

**3. Expected Output**
Displays result in the format:


{
  'score': 10,
  'percentage': 50.0,
  'grade': 'B'
}

_____________________________________________________________________________


**📂 Project Structure**


project/

│── exam_system.py

│── README.md

_____________________________________________________________________________

**🚀 Future Improvements**

Add timer-based auto submission

Support descriptive answer evaluation

Add database integration

Build a web interface

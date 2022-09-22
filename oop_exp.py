import random

class Question:
    
    def __init__(self,text,choices,correct_answer):
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    def check_answer(self,answer):
        return self.correct_answer == answer
        
q1 = Question("Atatürk Kaç Yılında Doğmuştur?",[1881,1882,1883,1880],1881)
q2 = Question("Atatürk Kaç Yılında Ölmüştür?",[1935,1934,1936,1938],1936)
q3 = Question("Cumhuriyet Kaç Yılında İlan Edilmiştir?",[1920,1921,1922,1923],1923)
q4 = Question("Türkiyeyinin Başkenti Neresidir?",['İstanbul','Konya','Ankara','İzmir'],'Ankara')
questions = [q1,q2,q3,q4]
random.shuffle(questions)

class Quiz:
    
    def __init__(self,questions):
        self.questions = questions
        self.score = 0
        self.question_index = 0

    def display_question(self):
        print(f"Soru {self.question_index + 1}: {self.questions[self.question_index].text}") 
        for i in range(len(self.questions[self.question_index].choices)):
            print(f"{chr(65+i)}: {self.questions[self.question_index].choices[i]}")   
        self.control_answer()

    def control_answer(self):
        ans = (input("Cevap: ")).upper()
        answer = self.questions[self.question_index].choices[ord(ans)-65]
        if self.questions[self.question_index].check_answer(answer):
            self.score += 1
        self.question_index += 1
        self.show_all_questions()    

    def show_all_questions(self):
        if len(self.questions) <= self.question_index:
            print(f"\nSkorunuz: {self.score}/{len(self.questions)}")
        else:
            self.display_question()     


quiz = Quiz(questions)   
quiz.display_question()
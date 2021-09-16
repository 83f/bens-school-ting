# quiz
# ben

from appJar import gui
import random

def press(btn):
        print(btn)
"""
Gui class and Question class combine to make a fun single question quiz
"""

# class definitions
class Question:
    # initilise class
        def __init__(self, question, answers, correct_answer):
                self.question = question
                self.answers = answers
                self.correct_answer = correct_answer      
                # returns True if correct answer is selected
                def check_correct(self, selected_answer):
                        _correct = True
                        return _correct
                # returns array of all possible answers
                def get_answer_array(self):
                        _answer_array = self.answers    
                        _answer_array.append(self.correct_answer)
                        return _answer_array
    # returns the answer text
def get_question_text(self):
        return self.question
    
class Gui:
        def __init__(self):
        #window setup
                app = gui("single question quiz", "800x600")
                app.setBg("orange")
                app.setFont(18)
                app.addlabelBg("question_text", "blue")
                app.addlabelFg("question_text", "orange")
                app.addLabel("question", "What’s the biggest ski area in the world?")
                app.addButton("Mt Hutt", press)
                app.addButton("4 Vallees", press)
                app.addButton("titanic 3 Vallees", press)
                app.addButton("milky way", press)
                app.addLabel("result","")
                self._app = app
                #run gui
                app.go()
                def display_question(self):
                        pass
def check_correct(press):
        print(self._app.getButton)
        if self._app.getButton == "titanic 3 Vallees": 
                self._app.setLabel("result","Correct")
        else:
                self._app.setLabel("result","Incorrect")

    
#main routine
quiz = Gui()
        
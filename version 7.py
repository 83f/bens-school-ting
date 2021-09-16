# quiz
# ben

from appJar import gui
import random
import time




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
                self._app = app
                app.setBg("orange")
                app.setFont(18)
                #frame setup
                with app.frame("q"):
                        #shows question + options.
                        app.addLabelBg("question_text", "blue")
                        app.addLabelFg("question_text", "orange")
                        app.addLabel("question", "What’s the biggest ski area in the world?")
                        app.addButton("Mt Hutt", self.press)
                        app.addButton("4 Vallees", self.press)
                        app.addButton("titanic 3 Vallees", self.press)
                        app.addButton("milky way", self.press)
                        
                        
                with app.frame("correct"):
                        app.addLabel("Cor","correct")
                #hides frame              
                app.hideFrame("correct")
                
                #adding new frame
                with app.frame("incorrect"):
                        app.addLabel("Incor","incorrect")
                        
                app.hideFrame("incorrect")                  
                
                #run gui
                app.go()
                
       
       
#shows incorrect or correct.
        def press(self, button):
                if button == "titanic 3 Vallees":
                        self._app.showFrame("correct")
                        self._app.hideFrame("q")
                if button == "Mt Hutt":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")        
                if button == "4 Vallees":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")   
                if button == "milky way":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")        
                        
                
                        
              


                
#while loop


#main routine
quiz = Gui()

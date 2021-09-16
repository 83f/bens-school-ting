# quiz
#Ben McInnes

from appJar import gui
import random
import sys


# variables

user_answers = []


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
        
 
def get_user_answers():
    answer_string = ""
    for answer in user_answers:
        
        answer_string += answer + "\n" 
  
  
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
                        
                        app.addLabel("question", "What’s the biggest ski area in the world?")
                        app.addButton("Mt Hutt", self.press)
                        app.addButton("4 Vallees", self.press)
                        app.addButton("titanic 3 Vallees", self.press)
                        app.addButton("milky way", self.press)
                        
                        
                with app.frame("q2"):
                        
                        #shows question + options.
                        
                        app.addLabel("question2", "In what year was the first winter olympics?")
                        app.addButton("1942", self.press)
                        app.addButton("1917", self.press)
                        app.addButton("1924", self.press)
                        app.addButton("1969", self.press)
                        app.hideFrame("q2")
                        
                        
                        
                with app.frame("correct"):                    
                        app.addLabel("Cor","correct")
                        app.addButtons(["next"], self.press)
                with app.frame("correct2"):
                    app.hideFrame("correct2")
                    app.addLabel("Cor2","Correct")
                    app.addButtons(["finish"], self.press)                
                #hides frame              
                app.hideFrame("correct")
                
                #adding new frame
                with app.frame("incorrect"):
                        app.addLabel("Incor","incorrect")
                        app.addButtons([" next "], self.press)
                with app.frame("incorrect2"):
                    app.hideFrame("incorrect2")
                    app.addLabel("Incor2","Incorrect")
                    app.addButtons(["Finish"], self.press)                
                        
                with app.frame("summary"):
                    app.hideFrame("summary")
                    app.addLabel("user_answers","")
                    app.addLabel("sumup","You made it to the end, You got 2 Answers Correct!")
                    
                    #self.get_user_answers()
                        
                app.hideFrame("incorrect")                  
                
                #run gui
 
                app.go()
                
       
       
#shows incorrect or correct.
        def press(self, button):
                if button == "titanic 3 Vallees":
                        self._app.showFrame("correct")
                        self._app.hideFrame("q")
                        user_answers.append(button)
                if button == "Mt Hutt":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")        
                if button == "4 Vallees":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")   
                if button == "milky way":
                        self._app.showFrame("incorrect")
                        self._app.hideFrame("q")    
                if button == "next":
                        self._app.showFrame("q2")
                        self._app.hideFrame("correct")
                        self._app.hideFrame("incorrect")
                if button == " next ":
                        self._app.showFrame("q2")
                        self._app.hideFrame("incorrect")
                        
                if button == "1924":                    
                        self._app.showFrame("correct2")
                        self._app.hideFrame("q2")
                        user_answers.append(button)
                if button == "1917":
                        self._app.showFrame("incorrect2")
                        self._app.hideFrame("q2")        
                if button == "1942":
                        self._app.showFrame("incorrect2")
                        self._app.hideFrame("q2")   
                if button == "1969":
                        self._app.showFrame("incorrect2")
                        self._app.hideFrame("q2")          
                if button == "finish":
                    self._app.showFrame("summary")
                    self._app.hideFrame("correct2")
                    # show summary frame
                    # set summary label to get_user_answers()
                if button == "Finish":
                    self._app.showFrame("summary")
                    self._app.hideFrame("incorrect2")
                    
                    # show summary frame
                    # set summary label to get_user_answers()                
                        
              
#main routine
quiz = Gui()

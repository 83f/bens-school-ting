#quizz 
#Ben McInnes


# import the library
from appJar import gui



# handle button events
def press(button):
    if button == "close":
        app.stop()
    if button == "titanic 3 Vallees":
        app.stop()
    if button == "next":
            app.stop()    

# create a GUI variable called app
app = gui("Skiing quiz", "600x200")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Test your skiing knowledge")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabel("question", "What’s the biggest ski area in the world?")
app.setLabelBg("question", "pink")



# link the buttons to the function called press
app.addButtons(["mt hutt", "titanic 3 Vallees", "Next", "close"], press)


#main routine
app.go()    

#correct

app = gui("Skiing quiz", "300x200")
app.setBg("yellow")
app.setFont(18)
app.addLabel("title", "correct")
app.addButtons(["next"], press)
app.go()

#question 2

app = gui("Skiing quiz", "600x200")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Test your skiing knowledge")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabel("question", "In what year was the first ever Winter Olympics?")
app.setLabelBg("question", "pink")

app.addButtons(["1924", "1917", "next", "close"], press)

app.go()
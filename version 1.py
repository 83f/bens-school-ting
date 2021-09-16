#quizz 
#Ben McInnes


# import the library
from appJar import gui

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        print("User:", usr, "Pass:", pwd)

# create a GUI variable called app
app = gui("Skiing quiz", "400x200")
app.setBg("yellow")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "Test your skiing knowledge")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "yellow")

app.addLabel("question", "")
app.setLabelBg("question", "pink")



# link the buttons to the function called press
app.addButtons(["A", "B", "Next", "Cancel"], press)


#main routine
app.go()    
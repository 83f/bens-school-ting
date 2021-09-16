#gui
#26/02/2021
#Ben McInnes

# import the library
from appJar import gui

#varivables
password_db = [['Admin' ,b'\xe3\xaf\xed\x00G\xb0\x80Y\xd0\xfa\xda\x10\xf4\x00\xc1\xe5'],
               ['Ben' ,b'\t/+\xa9\xf3\x9f\xbc(v\xe6M\x12\xcdf/r']]

# handle button events
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
        
        if usr == "Ben" and pwd == "root":
            print("access granted")

# create a GUI variable called app
app = gui("Login Window", "400x200")
app.setBg("orange")
app.setFont(18)

# add & configure widgets - widgets get a name, to help referencing them later
app.addLabel("title", "sorenhook")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")

# link the buttons to the function called press
app.addButtons(["Submit", "Cancel"], press)
app.setFocus("Username")

# start the GUI
app.go()
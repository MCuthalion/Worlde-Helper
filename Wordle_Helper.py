import pandas as pd

from kivy.app import App
#from kivy.properties import NumericProperty


class Wordle_HelperApp(App):

    # buttonRed = NumericProperty()
    # buttonGreen = NumericProperty()
    # buttonBlue = NumericProperty()

    def build(self):
        #work with a kivy file to build the gui
        pass

    def List(self):
        #Generates the list of words still available, populates, and calls the Popup
        pass
        print('test')

    def ButtonColor(self):
        #Changes the color the button when pressed to show correct letter or location
        #have RGB colors as NumericProperty()
        pass

    def CreateButtons(self):
        #create the row of 5 buttons that can be selected to show correct letter or location
        pass
        #or have all the buttons created already and just fill them? Could have distinct ID's and call programs easier



Wordle_HelperApp().run()
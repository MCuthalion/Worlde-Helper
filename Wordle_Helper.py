import pandas as pd

from kivy.app import App
from kivy.clock import Clock


class Wordle_Helper(App):


    def build(self):
        #work with a kivy file to build the gui
        global root
        global wordList
        wordList = []
        root = self.root
        root.ids.WordInput.focus = True

    def List(self):
        #Generates the list of words still available, populates, and calls the Popup
        pass
        print('List Test')

    def ButtonColor(self,x,y):
        #Cycles the button through the color options one click at a time
        i = 0
        for child in root.ids.ButtonGrid.children:
            if i == y:
                target = child
            i += 1

        i = 0
        for child in target.children:
            if i == x:
                if child.background_color == [1, 1, 1, 1.0]:
                    child.background_color = [1, 1, 0, 1.0]
                elif child.background_color == [1, 1, 0, 1.0]:
                    child.background_color = [0, 1, 0, 1.0]
                elif child.background_color == [0, 1, 0, 1.0]:
                    child.background_color = [1, 1, 1, 1.0]
            i += 1

    def FillButtons(self):
        #Fills the next row of buttons with the letters
        wordString = root.ids.WordInput.text
        if len(wordString) == 5 and len(wordList) < 6:
            wordList.append(wordString)

            if len(wordList) == 1:
                target = root.ids.WordFive
            elif len(wordList) == 2:
                target = root.ids.WordFour
            elif len(wordList) == 3:
                target = root.ids.WordThree
            elif len(wordList) == 4:
                target = root.ids.WordTwo
            elif len(wordList) == 5:
                target = root.ids.WordOne
            elif len(wordList) == 6:
                target = root.ids.WordZero

            i = 0
            for child in target.children:
                child.text = wordString[4-i]
                i += 1
        else:
            print('You messed Up!')


        root.ids.WordInput.text = ''
        Clock.schedule_once(lambda dt: self.FocusWidget())

    def FocusWidget(self):
        #Focuses the TextInput after Entry
        root.ids.WordInput.focus = True

Wordle_Helper().run()
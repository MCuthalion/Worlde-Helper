import pandas as pd

from kivy.app import App
from kivy.clock import Clock
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class Wordle_Helper(App):


    def build(self):
        #initializes the app
        global root
        global wordList
        global df
        root = self.root
        wordList = []
        df = pd.DataFrame()
        df = pd.read_csv('Words.csv')
        root.ids.WordInput.focus = True

    def List(self):
        #Generates the list of words still available, populates, and calls the Popup

        #Read the letters from the buttons and the colors
        excludedLetter = []
        quasiLetter = []
        exactLetter = []
        temp = []

        for child in root.ids.ButtonGrid.children:
            l = 4
            for kid in child.children:
                if kid.text != "":
                    if kid.background_color == [1, 1, 1, 1.0]:
                        excludedLetter.append(kid.text)
                    elif kid.background_color == [1, 1, 0, 1.0]:
                        temp.append(kid.text)
                        temp.append(l)
                        quasiLetter.append(temp)
                        temp = []
                    elif kid.background_color == [0, 1, 0, 1.0]:
                        temp.append(kid.text)
                        temp.append(l)
                        exactLetter.append(temp)
                        temp = []
                l -= 1

        print('Excluded Letters')
        print(excludedLetter)
        print('Quasi Letters')
        print(quasiLetter)
        print('Exact Letters')
        print(exactLetter)

        #parse the dataframe
        df_words = pd.DataFrame()
        df_words = df
        for letter in excludedLetter:
            df_words = df_words.drop(df_words[df_words.Letter1 == letter].index)
            df_words = df_words.drop(df_words[df_words.Letter2 == letter].index)
            df_words = df_words.drop(df_words[df_words.Letter3 == letter].index)
            df_words = df_words.drop(df_words[df_words.Letter4 == letter].index)
            df_words = df_words.drop(df_words[df_words.Letter5 == letter].index)

        for letter in quasiLetter:
            pass
            #Letter has to be present in another column but not this one
            if letter[1] == 0:
                #drop all rows where letter1 is that letter
                df_words = df_words.drop(df_words[df_words.Letter1 == letter[0]].index)
                #Then iterate through and drop rows where a letter isn't found

        for letter in exactLetter:
            if letter[1] == 0:
                df_words = df_words.drop(df_words[df_words.Letter1 != letter[0]].index)
            elif letter[1] == 1:
                df_words = df_words.drop(df_words[df_words.Letter2 != letter[0]].index)
            elif letter[1] == 2:
                df_words = df_words.drop(df_words[df_words.Letter3 != letter[0]].index)
            elif letter[1] == 3:
                df_words = df_words.drop(df_words[df_words.Letter4 != letter[0]].index)
            elif letter[1] == 4:
                df_words = df_words.drop(df_words[df_words.Letter5 != letter[0]].index)

        print(df_words.tail())


        #display popup and print the list

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
            popup = Popup(size_hint_x=0.5,size_hint_y=0.5,title='',separator_height=0)
            label = Label(text='That word is not 5 letters long\nOr you have entered too many words')
            popup.add_widget(label)
            popup.open()


        root.ids.WordInput.text = ''
        Clock.schedule_once(lambda dt: self.FocusWidget())

    def FocusWidget(self):
        #Focuses the TextInput after Entry
        root.ids.WordInput.focus = True

Wordle_Helper().run()
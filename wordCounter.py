from tkinter import *
from itertools import count
import re
import tkinter
from tkinter.filedialog import *
from urllib.request import OpenerDirector

from setuptools import Command


def getFile():
    path = askopenfilename()
    if path != "":
        outputFileName = path + "-word rank by Giovani Drosda Lima.txt"
        outputFile = open(outputFileName, "w")

        fileSrc = open(path, "rt")
        file = fileSrc.read()

        noDotsText = re.sub(r"[^a-zA-Z0-9-\s]", "", file)
        #noDotsText = re.sub('["]', "", file)

        listOfWords = re.split("\s", noDotsText)
        listOfWordsCounted = list()
        listOfWordsWithCountDict = {}

        for eachWord in listOfWords:
            if eachWord not in listOfWordsCounted:
                x = listOfWords.count(eachWord)
                listOfWordsCounted.append(eachWord)
                listOfWordsWithCountDict[eachWord] = x


        sortedList = sorted(listOfWordsWithCountDict.items(), key=lambda x: (1-x[1], x[0]))
        for item in sortedList:
            #print(item, "\n")
            line = str(item) + "\n"
            outputFile.write(line)

        outputFileWidget = Label(outputFileWindow, text="Saved as " + outputFileName)
        outputFileWidget.pack()
        
        fileSrc.close()
        outputFile.close()

outputFileWindow = Tk()
outputFileWindow.title("Word counter by Giovani Drosda Lima v0.1 beta")
chooseFileButton = Button(outputFileWindow, text="Click here to choose a file", padx=100, pady=40, command=getFile)
chooseFileButton.pack()
outputFileWindow.mainloop()



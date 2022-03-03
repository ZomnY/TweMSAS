# Project: Masters Thesis 
# 
# TweMSAS - Tweet Manual Sentiment Analysis Scoring Program
#
# start date coding: 26.02.2022
# author: Johannes Wellhöfer
# file execution order: - none - 

""" This program was built for manual tweet text sentiment scoring for the master thesis of Johannes Wellhöfer. 
Whomever finds this useful, may use it :)

read the readme in the files
"""

#--------------------------------------------
# Import #####
#----------
# Packages ###
from tkinter import *
import csv
import os

root = Tk()

#----------
# Data ###
# read file
outputPath = './output/results.csv'

count = 0

fileExists = os.path.isfile(outputPath)

if fileExists:
    with open(outputPath, 'r', encoding='utf8') as fp:
        for count, line in enumerate(fp):
            pass
    print('Total Lines', count + 1)

dataPosition = IntVar()
dataPosition.set(count - 1)
data = []

with open('./data/tweets.csv', newline='', encoding='utf8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data.append(row)


#--------------------------------------------
# Variables #####
tweetTextLabel = Text(root, height=5, width=100)

# tweetText = StringVar()
sentimentPolarity = IntVar()
sentimentPolarity.set(0)
ironyOrSarcasm = IntVar()
ironyOrSarcasm.set(0)
memeOrDomain = IntVar()
memeOrDomain.set(0)


#--------------------------------------------
# Functions #####

def loadTweet(tweetDict):
    # tweetText.set("....................\n" + tweetDict["text"] + "\n....................")
    tweetTextLabel.configure(state="normal")
    tweetTextLabel.delete('1.0', END)
    tweetTextLabel.insert(END, tweetDict["text"])
    tweetTextLabel.configure(state="disabled")

def loadNextTweet():
    global dataPosition
    dataPosition.set(dataPosition.get() + 1)
    loadTweet(data[dataPosition.get()])

loadNextTweet()

def submitScoring(tweetDict):
    global sentimentPolarity, ironyOrSarcasm, memeOrDomain, outputPath, fileExists

    fileExists = os.path.isfile(outputPath)

    with open(outputPath, 'a', newline='', encoding='utf8') as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=['author_id', 'tweet_id', 'text', 'sentiment_polarity', 'irony_or_sarcasm', 'meme_or_domain', 'created_at'])

        if not fileExists:
            writer.writeheader()
        
        writer.writerow({
            'author_id': tweetDict['author_id'],
            'tweet_id': tweetDict['\ufefftweet_id'],    # this is an ugly ass mod, because the data was stored as UTF8 for the special characters.
                                                        # this apparently appends an utf8 signifier in front of the first line (which has the tweet_id as first cell)
                                                        # this utf8 signifier is "\ufeff"
            'text': tweetDict['text'],
            'sentiment_polarity': sentimentPolarity.get(),
            'irony_or_sarcasm': ironyOrSarcasm.get(),
            'meme_or_domain': memeOrDomain.get(),
            'created_at': tweetDict['created_at']
        })

    sentimentPolarity.set(0)
    ironyOrSarcasm.set(0)
    memeOrDomain.set(0)

    loadNextTweet()

def submitNotEnglishEvent():
    global sentimentPolarity, ironyOrSarcasm, memeOrDomain
    sentimentPolarity.set(-99)
    ironyOrSarcasm.set(0)
    memeOrDomain.set(0)
    submitScoring(data[dataPosition.get()])

def submitUnclearEvent():
    global sentimentPolarity, ironyOrSarcasm, memeOrDomain
    sentimentPolarity.set(-97)
    ironyOrSarcasm.set(0)
    memeOrDomain.set(0)
    submitScoring(data[dataPosition.get()])

def submitScoringEvent():
    submitScoring(data[dataPosition.get()])



#--------------------------------------------
# Tkinter #####
#----------
# Widgets ###

# Main Window
root.title('TweMSAS - Tweet Manual Sentiment Analysis Scoring')
# root.geometry('1700x900+150+100')
root.iconphoto(False, PhotoImage(file='icon.png'))
# root.resizable(False, False)

# Labels #
dataPositionLabel = Label(root, textvariable=dataPosition)
doLabel = Label(root, text="Indicate the sentiment polarity, sarcasm, and domain relevance for the displayed text.")
textTweetTextLabel = Label(root, text="Tweet text: ")
textTweetResponseLabel = Label(root, text="Tweet in response to: ")
emptyLabel = Label(root, text="     ")
# tweetTextLabel = Label(root, textvariable=tweetText)
# tweetTextLabel = Label(root, text=complimentLineTxt)

# Checkboxes #
ironyORsarcasmButton = Checkbutton(root, text="[q] Irony or sarcasm content", variable=ironyOrSarcasm, onvalue=1, offvalue=0)
memeORdomainButton = Checkbutton(root, text="[e] Meme or domain content", variable=memeOrDomain, onvalue=1, offvalue=0) 



# Sentiment Buttons
negativeButton = Radiobutton(root, text="[1] negative (-2)", variable=sentimentPolarity, value=-2) 
slightNegativeButton = Radiobutton(root, text="[2] slightly negative (-1)", variable=sentimentPolarity, value=-1) 
neutralButton = Radiobutton(root, text="[3] neutral (0)", variable=sentimentPolarity, value=0) 
slightPositiveButton = Radiobutton(root, text="[4] slightly positive (+1)", variable=sentimentPolarity, value=1) 
positiveButton = Radiobutton(root, text="[5] positive (+2)", variable=sentimentPolarity, value=2) 

# Next Buttons
notEnglishButton = Button(root, text="text not english (next)", command=submitNotEnglishEvent) 
unclearButton = Button(root, text="content unclear (next)", command=submitUnclearEvent) 
submitButton = Button(root, text="Submit", command=submitScoringEvent) # , command=submitTweetScoring

#----------
# Packing ###
doLabel.grid(row=1, column=1)
emptyLabel.grid(row=2, column=1)
tweetTextLabel.grid(row=3, column=1)
emptyLabel.grid(row=4, column=1)

textTweetTextLabel.grid(row=3 , column=0)
textTweetResponseLabel.grid(row= 2, column=0)

unclearButton.grid(row=5 , column=2)
notEnglishButton.grid(row=7 , column=2)

negativeButton.grid(row=5 , column=0)
slightNegativeButton.grid(row=6 , column=0) 
neutralButton.grid(row=7 , column=0) 
slightPositiveButton.grid(row=8 , column=0) 
positiveButton.grid(row=9 , column=0) 

dataPositionLabel.grid(row=9, column=1)

ironyORsarcasmButton.grid(row=5, column=1)
memeORdomainButton.grid(row=7, column=1)

submitButton.grid(row=11, column=2)

root.bind('1', lambda event: sentimentPolarity.set(-2))
root.bind('2', lambda event: sentimentPolarity.set(-1))
root.bind('3', lambda event: sentimentPolarity.set(0))
root.bind('4', lambda event: sentimentPolarity.set(1))
root.bind('5', lambda event: sentimentPolarity.set(2))

root.bind('q', lambda event: ironyOrSarcasm.set((ironyOrSarcasm.get() + 1) % 2))
root.bind('e', lambda event: memeOrDomain.set((memeOrDomain.get() + 1) % 2))

#----------
# creating EVENTLOOP #####
root.mainloop()
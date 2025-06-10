import random
import readquiz
from tkinter import *

rounds = 0
ansright = 0

initializer = Tk()

formatter = Label(initializer)
formatter['text'] = 'Question:'
formatter.pack()

labelmess = Message(initializer, width=200)
labelmess['text'] = ''
labelmess.pack()

ans = Frame(initializer)
yesbut = Button(ans)
yesbut['text']='Yes'
yesbut.pack(side=LEFT, expand=YES, fill=X)

nobut = Button(ans)
nobut['text']='No'
nobut.pack(side=RIGHT, expand=YES, fill=X)

ans.pack(fill=X)

status = Frame(initializer)
resp = Label(status)
scorekeeper = Label(status)

resp['text'] = 'Status'
scorekeeper['text'] = 'Score: 0/0'

resp.pack(side=LEFT)
scorekeeper.pack(side=RIGHT)

status.pack(fill=X)

questionloader = readquiz.loadQuestions()

def is_correct():
    resp['text'] = 'Your answer was correct'
    resp['bg'] = 'light green'
    global rounds, ansright
    rounds += 1
    ansright += 1
    scorekeeper['text'] = 'Score: {}/{}'.format(ansright, rounds)
    ques()

def is_incorrect():
    resp['text'] = 'Your answer was incorrect'    
    resp['bg'] = 'pink'
    global rounds
    rounds += 1
    scorekeeper['text'] = 'Score: {}/{}'.format(ansright, rounds)
    ques()

def ques():
    z = random.choice(questionloader)
    a = z[0]
    ans = z[1]
    labelmess['text'] = a
    if ans:
        yesbut['command'] = is_correct
        nobut['command'] = is_incorrect
    else:
        yesbut['command'] = is_incorrect
        nobut['command'] = is_correct

ques()

mainloop()

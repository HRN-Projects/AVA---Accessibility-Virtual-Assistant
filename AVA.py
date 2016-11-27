import sys, math, random, pyttsx, webbrowser, datetime, time, urllib2, string
from bs4 import *
import speech_recognition as sr
from PyQt4 import QtGui, QtCore

########################################################### Checking lists ##############################################################################################

conjunctions = ['For','And','Nor','But','Or','Yet','So','After','Although','As', 'Because','Before','If','Once','Since','Though','Unless','Until','When','Where','While']
prepositions = ['About','Above','Across','After','Against','Along','Amid','Among','Around','At','Before','Behind','Below','Beneath','Beside','Besides','Between','Beyond','By','Down','In','Inside','Into','Near','Of','Off','On','Onto','Opposite','Outside','Over','Past','To','Toward','Towards','Under','Underneath','Until','Up','Upon','Versus','Via','With','Within']
articles = ['A','An','The']

########################################################### Conversation lists ##########################################################################################
greets = ['hi','hello','hello there','hi there','hey','hey there','namaste','hola']

    # Questions / Queries - 
helpcom = ['show all commands','show help', 'help', 'show commands' , 'show help commands', 'all commands']
info = ['summarize the project', 'Project summary', 'tell me something about you in details' ,'details about you', 'your project summary','project summary and details','project details']
closing = ['terminate conversation','terminate now','exit chat', 'exit now', 'terminate', 'close chat', 'close conversation', 'close yourself', 'exit conversation', 'end now', 'end chat', 'end conversation']
botcall = ['how is everything Jarvis','Jarvis how are you','how are you', 'how are you Jarvis', 'how are you doing', 'how are you doing Jarvis', 'how is everything going on',"what's up Jarvis"]
frequest = [['what is the time right now',"what's the time right now",'what time is it right now',"what's the time", 'what time is it in the clock', 'what is the time', "what's the time now", 'what time is it now', 'tell me the time'], ["what's the date today", 'what is the date today', "today's date is", "tell me today's date", "today's date is"], ["what is today's day", "what's today's day", 'what is the day today', "today's day is", "tell me today's day"]]
greets2 = ['hey Jarvis', 'hi Jarvis', 'hello Jarvis']
readycheck = ['Jarvis', 'you there Jarvis', 'are you there Jarvis','jarvis are you there', 'jarvis you there', 'are you ready', 'jarvis are you ready', 'you ready Jarvis', 'jarvis you ready']
botintro = ['who are you', "what's your name", 'who am I talking to', 'what are you', 'what is your name', 'what are you called', 'what do people call you']

    # Bot Replies - 
botans = ['I am fine...', 'I am doing great...', 'I\'m fine, thank you...' ,'I am glad you asked, thank you...', 'Everything is good... thank you...', 'Everything is great...', 'Everything Seems normal and under control...']
compos = ['At your service', 'Ask me', 'Waiting for your command', 'Tell me something to do', 'How can I help you?']
byes = ['until next time', 'bye bye', 'see you soon', 'chao', 'goodbye', 'catch you later', 'see you next time']
introans = ['I am Jarvis, your virtual personal assistant', 'They call me "Jarvis"', 'People call me "Jarvis"', 'My name is Jarvis']
readyans = ['I am online and ready...', 'Ready', 'Up and running...', 'Always ready to help and assist...']
projectDetails = "AVA (Accessibility Virtual Assistant) is a virtual assistant developed for better accessiblity and interactivity in an open source environment. This vitual assistant is used to perform some regular tasks like - Getting Date, Time or Day, Simple arithmetic calculations, and Even searching almost anything on internet. These tasks can be performed just by using some voice commands. The project is developed in python."

############################################### Properties and objects for various modules ############################################################################
Bot = "J.A.R.V.I.S "

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)

mic_recog = sr.Recognizer()
mic = sr.Microphone()
                                
############################################################ Date, Day and Time calculation methods #####################################################################
now = datetime.datetime.now()
t1 = ''

def tick():
    global t1
    t2 = time.strftime("%I:%M:%S %p")
    if t2 != t1:
        t1 = t2

def timing():
    tick()
    reply = ("Current time is " + t1)
    engine.say(reply)
    txt1 = txt.toPlainText()
    txt.insertPlainText(Bot + " :\nTime is : " + reply  + "\n")
    engine.runAndWait()

date = now.strftime("%d-%B-%Y")
day = now.strftime("%A")

######################################################################### Program GUI #################################################################################
class guiWindow(QtGui.QMainWindow):

    def __init__(self):
        super(guiWindow, self).__init__()
        self.setGeometry(300,150,750,500)
        self.setWindowTitle("PyQt Gui test Window")
        self.setWindowIcon(QtGui.QIcon("bgimg.jpg"))
        self.setStyleSheet('background-color: #ffff66;')
        self.setFixedSize(750,500)
        
        global txt
        
        txt = QtGui.QTextEdit(self)
        txt.setStyleSheet("QTextEdit {background-color: white; color: black; font-size: 14px; font-weight: bold;}")
        txt.setGeometry(100,90,550,300)
        txt.setReadOnly(1)

        self.process = QtGui.QProgressBar(self)
        self.process.setGeometry(100,400,585,30)

        #self.closebtn()
        self.prnt()
        self.show()
        
    """def closebtn(self):
        btn = QtGui.QPushButton("Close Window", self)
        btn.setStyleSheet('QPushButton {background-color: #0033cc; color: white; font-weight: bold; font-size: 18px;}')
        btn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        btn.setGeometry(0,350,600,50)
        btn.show()"""

    def prnt(self):
        btn1 = QtGui.QPushButton("Start !", self)
        btn1.setStyleSheet('QPushButton {background-color: #ff7733; color: white; font-weight: bold; font-size: 14px;}')
        btn1.clicked.connect(self.ava)
        btn1. resize(100,50)
        btn1.move(320,30)
        btn1.show()
        
################################################################# Main program body ###################################################################################
    def ava(self):
        try:
            with mic as source: mic_recog.adjust_for_ambient_noise(source)
            txt.insertPlainText("Minimum enery threshold is : {}".format(mic_recog.energy_threshold))

            engine.say("Welcome to the interactive chatroom !")                      # User interaction starts here
            start = "\nWelcome to the interactive chatroom !"
            reply = (start) 
            txt.insertPlainText(reply)
            engine.runAndWait()
            
            while True:
                txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())
                quest = random.choice(compos)
                engine.say(quest)
                txt.insertPlainText("\n\n" + quest + " : \n")
                engine.runAndWait()
                txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())
                with mic as source: audio = mic_recog.listen(source)
                process = ("Processing...\n")
                txt.insertPlainText(process)
                self.completed = 0
                while self.completed<100:
                    self.completed += 0.001
                    self.process.setValue(self.completed)
                try:
                    value = mic_recog.recognize_google(audio)

                    if str is bytes:                                                                        # For Python 2.x
                        comms = "{}".format(value).encode("utf-8")
                        u = "You"
                        reply = "\n" + u + " :\n" + comms + "  \n"
                        txt.insertPlainText(reply)
                                                                                                                # Starts checking for the reply from here
                        if comms in greets or comms in greets2:                              # If Command was a greeting
                            reply = random.choice(greets)
                            engine.say(reply)
                            txt.insertPlainText( Bot+ " :\n" + reply.capitalize() + "!\n")
                            engine.runAndWait()
                            
                        if comms in info:
                            reply = projectDetails
                            engine.say(reply)
                            txt.insertPlainText(Bot + " :\n" + reply + "\n")
                            engine.runAndWait()
                            
                        elif comms in helpcom:                                                      # If command was to list all available commands
                            reply = "Following commands are stored for interaction and usage right now..."
                            engine.say(reply)
                            txt.insertPlainText( Bot + " :\n" + reply + "\n")

                            print("Greeting commands -")
                            for i in range(8):
                                reply = greets[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            for i in range(3):
                                reply = greets2[i]                                
                                txt.insertPlainText( "\t-> " + reply + "\n")
                                
                            print("\nIntroductory commands -")
                            for i in range(7):
                                reply = botintro[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            print("\nClosing commands -")
                            for i in range(12):
                                reply = closing[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            print("\nInteraction commands -")
                            for i in range(5):
                                reply = botcall[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")
                                
                            for i in range(9):
                                reply = readycheck[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            print("\nTime, Date and Day commands -")
                            for i in range(9):
                                reply = frequest[0][i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            for i in range(5):
                                reply = frequest[1][i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            for i in range(5):
                                reply = frequest[2][i]
                                txt.insertPlainText( "\t-> " + reply + "\n")
                                
                            print("\n Project info commands -")
                            for i in range(6):
                                reply = info[i]
                                txt.insertPlainText( "\t->" + reply + "\n")
                            
                            for i in range(5):
                                reply = teamcom[i]
                                txt.insertPlainText( "\t-> " + reply + "\n")

                            txt.insertPlainText("\n##### END OF COMMANDS #####\n")
                            engine.runAndWait()
                            
                        elif comms in botintro:                                                 # Commands for bot intro
                            reply = random.choice(introans)
                            engine.say(reply)                            
                            txt.insertPlainText( Bot + " :\n"  + reply)

                        elif comms in botcall:                                                  # Interactive commands
                            reply = random.choice(botans)
                            engine.say(reply)                            
                            txt.insertPlainText( Bot + " :\n"  + reply)
                            engine.runAndWait()

                        elif comms in readycheck:                                           # Interactive commands
                            reply = random.choice(readyans)
                            engine.say(reply)                            
                            txt.insertPlainText( Bot + " :\n"  + reply)
                            engine.runAndWait()

                        elif comms in frequest[0]:                                          # Commands to know - Time, Date or Day.
                            timing()

                        elif comms in frequest[1]:
                            reply = date
                            engine.say("Today's date is " + reply)                       
                            txt.insertPlainText( Bot + " :\n"  + "today's date is : " + reply + "\n")
                            engine.runAndWait()

                        elif comms in frequest[2]:
                            reply = day
                            engine.say("The day today is : " + reply)                            
                            txt.insertPlainText( Bot + " :\n"  + "The day today is - " + reply + "\n")
                            engine.runAndWait()
                            
                        elif (comms in closing) or (comms in byes):                                              # Commands to Exit program
                            reply = random.choice(byes)
                            engine.say(reply)
                            
                            txt.insertPlainText( Bot + " :\n"  + reply.capitalize() + "...\n")
                            engine.runAndWait()
                            sys.exit()

                        elif ('define' in comms) or (('what' and 'is') in comms) or (('who' and 'is') in comms):                    # Use 'Define', 'who is' or 'what is' to find any definition online.
                            try:
                                commlist = (string.capwords(comms)).split()
                                listlen = len(commlist)
                                if ((commlist[0]=='Define') and (listlen<=1)) or (((commlist[0]=='What' and commlist[1]=='Is') or (commlist[0]=='Who' and commlist[1]=='Is')) and (listlen<=2)):
                                    raise
                                
                                elif (commlist[0]=='Define') or (commlist[0]=='What' and commlist[1]=='Is') or (commlist[0]=='Who' and commlist[1]=='Is'):
                                    for x in range(listlen-1):
                                        if commlist[x] in conjunctions or commlist[x] in prepositions or commlist[x] in articles:
                                            commlist[x] = commlist[x].lower()

                                    if commlist[0]=='Define':
                                        commlist.remove('Define')
                                    elif (commlist[0]=='What' and commlist[1]=='Is'):
                                        commlist.remove('What')
                                        commlist.remove('Is')
                                    elif (commlist[0]=='Who' and commlist[1]=='Is'):
                                        commlist.remove('Who')
                                        commlist.remove('Is')
                                        
                                    searchstr = "_".join(commlist)
                                    try:
                                        txt.verticalScrollBar().setValue(txt.verticalScrollBar().maximum())
                                        wiki_search = ("https://en.wikipedia.org/wiki/" + searchstr)
                                        page = urllib2.urlopen(wiki_search)
                                        soup = BeautifulSoup(page, "html.parser")

                                        reply = soup.find('h1', {'class' : 'firstHeading'})
                                        txt.insertPlainText ( "\n" + reply.text + ":-\n")
                                        engine.say(reply.text)
                                        reply = soup.find('p')
                                        txt.insertPlainText( "\t" + reply.text + "\n")
                                        engine.say(reply.text)
                                    
                                    except:
                                        reply = comms
                                        engine.say("Couldn't find "  + reply)                                        
                                        txt.insertPlainText( "Couldn't find "  + reply + "...\n")
                                        engine.runAndWait()

                            except:                                
                                txt.insertPlainText( 'Sorry, couldn\'t understand that...\nPlease try again...')

                        elif 'calculate' in comms:                                                                                                                              # 'Calculate' for calculating arithmetic operations
                            commlist = comms.split()
                            try:
                                if (commlist[2]=='+') or (commlist[2]=='subtracted') or (commlist[2]=='added') or (commlist[2]=='times') or (commlist[2]=='multiplied') or (commlist[2]=='divided') or (commlist[2]=='into') or (commlist[2]=='upon') or (commlist[2]=='minus') or (commlist[2]=='by') or (commlist[2]=='x') or (commlist[2]=='-') or (commlist[2]=='/'):
                                    global opr
                                    opr = commlist[2]

                                    # Basic arithmetic calculations -
                                    def calc():
                                        if (opr=='+') or (opr=='added') or (opr=='plus'):
                                            res = num1 + num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The sum would be ' + sol)
                                            engine.say('The sum would be ' + sol)                                            
                                            txt.insertPlainText( Bot + " :\n"  + n1 + ' + ' + n2 + ' = ' + sol + "\n")
                                            
                                        elif (opr=='-') or (opr=='minus') or (opr=='subtracted'):
                                            res = num1 - num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The difference would be ' + sol)
                                            engine.say('The difference would be ' + sol)                                            
                                            txt.insertPlainText( Bot + " :\n"  + n1 + ' - ' + n2 + ' = ' + sol + "\n")
                                            
                                        elif (opr=='x') or (opr=='into') or (opr=='multiplied') or (opr=='times'):
                                            res = num1 * num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The product would be ' + sol)
                                            engine.say('The product would be ' + sol)                                            
                                            txt.insertPlainText( Bot + " :\n"  + n1 + ' x ' + n2 + ' = ' + sol + "\n")
                                            
                                        elif (opr=='/') or (opr=='divided') or (opr=='upon') or (opr=='by'):
                                            res = num1 / num2
                                            n1 = str(num1)
                                            n2 = str(num2)
                                            sol = str(res)
                                            reply = ('The result of division would be ' + sol)
                                            engine.say('The result would be ' + sol)
                                            txt.insertPlainText( Bot + " :\n"  + n1 + ' / ' + n2 + ' = ' + sol + "\n")
                                            
                                        else:
                                            reply = "Only four basic arithmetic operations allowed right now..."
                                            engine.say(reply)                                            
                                            txt.insertPlainText( reply + "\n")
                                            engine.runAndWait()

                                    if (commlist[3]=='to') or (commlist[3]=='by') or (commlist[3]=='with'):
                                        oprprep = commlist[3]
                                        num1 = float(commlist[1])
                                        num2 = float(commlist[4])
                                        calc()
                                    else:
                                        num1 = float(commlist[1])
                                        num2 = float(commlist[3])
                                        calc()
                            
                            except:
                                txt.insertPlainText( 'Sorry, couldn\'t understand that...\nPlease try again...')
                                
                        else:
                            txt.insertPlainText( Bot + " =>\n"  + "You said : '" + comms + "'\n")
                            
                    else:                                                       # For Python 3.x
                        comms = ("{}".format(value))
                        print("You -> " + comms)
                        
                        if comms in greets:
                            random_greets = random.choice(greets)
                            engine.say(random_greets)
                            print("Jarvis -> " + random_greets)
                            engine.runAndWait()

                        elif comms=="exit now":
                            engine.say("Until next time, Bye Bye!")
                            print("Until next time, Bye Bye!")
                            engine.runAndWait()
                            sys.exit()

                except sr.UnknownValueError:
                    reply = "Oops! Couldn't get that...\n"
                    txt.insertPlainText(reply)
                    
                except sr.RequestError as e:
                    reply = "Sorry, can't process at this time... Check your internet connection...\nTerminating the program...\n"
                    engine.say(reply)
                    txt.insertPlainText(reply)
                    engine.runAndWait()
                    sys.exit()

        except KeyboardInterrupt:
            pass
        
def run():
    app = QtGui.QApplication(sys.argv)
    GUI = guiWindow()
    sys.exit(app.exec_())

run()

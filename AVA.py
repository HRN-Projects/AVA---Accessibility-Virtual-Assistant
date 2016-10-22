import sys, math, random, pyttsx, webbrowser, datetime, time, urllib2, string
from bs4 import *
import speech_recognition as sr

############################################### Properties and objects for various modules ############################################################################
Bot = "J.A.R.V.I.S => "

engine = pyttsx.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-60)

mic_recog = sr.Recognizer()
mic = sr.Microphone()

# Basic arithmetic calculations -
def calc():
    if (opr=='+') or (opr=='added') or (opr=='plus'):
        res = num1 + num2
        n1 = str(num1)
        n2 = str(num2)
        sol = str(res)
        engine.say('The sum would be ' + sol)
        print (n1 + ' + ' + n2 + ' = ' + sol)
    elif (opr=='-') or (opr=='minus') or (opr=='subtracted'):
        res = num1 - num2
        n1 = str(num1)
        n2 = str(num2)
        sol = str(res)
        engine.say('The difference would be ' + sol)
        print (n1 + ' - ' + n2 + ' = ' + sol)
    elif (opr=='x') or (opr=='into') or (opr=='multiplied') or (opr=='times'):
        res = num1 * num2
        n1 = str(num1)
        n2 = str(num2)
        sol = str(res)
        engine.say('The product would be ' + sol)
        print (n1 + ' * ' + n2 + ' = ' + sol)
    elif (opr=='/') or (opr=='divided') or (opr=='upon') or (opr=='by'):
        res = num1 / num2
        n1 = str(num1)
        n2 = str(num2)
        sol = str(res)
        engine.say('The result would be ' + sol)
        print (n1 + ' / ' + n2 + ' = ' + sol)
    else:
        engine.say("Only four basic arithmetic operations allowed right now...")
        print ("Only four basic arithmetic operations allowed right now...")
    engine.runAndWait()
                                
# Date, Day and Time calculation methods -
now = datetime.datetime.now()
t1 = ''

def tick():
    global t1
    t2 = time.strftime("%I:%M:%S %p")
    if t2 != t1:
        t1 = t2

def timing():
    tick()
    engine.say("Current time is " + t1)
    print(Bot + "Time is : " + t1 + "\n")
    engine.runAndWait()

date = now.strftime("%d-%B-%Y")
day = now.strftime("%A")

########################################################### Checking lists ##############################################################################################

conjunctions = ['For','And','Nor','But','Or','Yet','So','After','Although','As', 'Because','Before','If','Once','Since','Though','Unless','Until','When','Where','While']
prepositions = ['About','Above','Across','After','Against','Along','Amid','Among','Around','At','Before','Behind','Below','Beneath','Beside','Besides','Between','Beyond','By','Down','In','Inside','Into','Near','Of','Off','On','Onto','Opposite','Outside','Over','Past','To','Toward','Towards','Under','Underneath','Until','Up','Upon','Versus','Via','With','Within']
articles = ['A','An','The']

########################################################### Conversation lists ##########################################################################################
greets = ['hi','hello','hello there','hi there','hey','hey there','namaste','hola']

    # Questions / Queries - 
helpcom = ['show all commands','show help', 'help', 'show commands' , 'show help commands', 'all commands']
info = ['summarize the project', 'Project summary', 'tell me something about you in details' ,'details about you', 'your project summary','project summary and details']
teamcom = ['who created you', 'people who built you', 'people behind your creation', 'team members of your project', 'people of the project']
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

################################################################# Main program body ###################################################################################

try:
    with mic as source: mic_recog.adjust_for_ambient_noise(source)
    print("Minimum enery threshold is : {}".format(mic_recog.energy_threshold))

    engine.say("Welcome to the interactive chatroom !")                      # User interaction starts here
    print("Welcome to the interactive chatroom !")
    engine.runAndWait()

    while True:
        random_comms = random.choice(compos)
        engine.say(random_comms)
        print("\n" + random_comms + " : ")
        engine.runAndWait()
        with mic as source: audio = mic_recog.listen(source)
        print("processing...")
        
        try:
            value = mic_recog.recognize_google(audio)

            if str is bytes:                                                                        # For Python 2.x
                comms = "{}".format(value).encode("utf-8")
                print(" You => " + comms)
                                                                                                        # Starts checking for the reply from here
                if comms in greets or comms in greets2:                              # If Command was a greeting
                    random_greet = random.choice(greets)
                    engine.say(random_greet)
                    print(Bot + random_greet.capitalize() + "!\n")
                    engine.runAndWait()
                    
                elif comms in helpcom:                                                      # If command was to list all available commands
                    engine.say("Following commands are stored for interaction and usage right now...")
                    print(Bot + " \nFollowing commands are stored for interaction and usage right now - \n")

                    print("Greeting commands -")
                    for i in range(8):
                        print("\t-> " + greets[i])
                    for i in range(3):
                        print("\t-> " + greets2[i])
                        
                    print("\nIntroductory commands -")
                    for i in range(7):
                        print("\t-> " + botintro[i])

                    print("\nClosing commands -")
                    for i in range(12):
                        print("\t-> " + closing[i])

                    print("\nInteraction commands -")
                    for i in range(5):
                        print("\t-> " + botcall[i])
                    for i in range(9):
                        print("\t-> " + readycheck[i])

                    print("\nTime, Date and Day commands -")
                    for i in range(9):
                        print("\t-> " + frequest[0][i])
                    print("\n")

                    for i in range(5):
                        print("\t-> " + frequest[1][i])
                    print("\n")

                    for i in range(5):
                        print("\t-> " + frequest[2][i])
                        
                    print("\n Project info commands -")
                    for i in range(6):
                        print("\t->" + info[i])
                    print("\n")
                    for i in range(5):
                        print("\t-> " + teamcom[i])

                    print("\n######################## END OF COMMANDS #############################\n")
                    engine.runAndWait()
                    
                elif comms in botintro:                                                 # Commands for bot intro
                    random_teller = random.choice(introans)
                    engine.say(random_teller)
                    print(Bot + random_teller)

                elif comms in botcall:                                                  # Interactive commands
                    random_botans = random.choice(botans)
                    engine.say(random_botans)
                    print(Bot + random_botans)
                    engine.runAndWait()

                elif comms in readycheck:                                           # Interactive commands
                    random_ans = random.choice(readyans)
                    engine.say(random_ans)
                    print(Bot + random_ans)
                    engine.runAndWait()

                elif comms in frequest[0]:                                          # Commands to know - Time, Date or Day.
                    timing()

                elif comms in frequest[1]:
                    engine.say("Today's date is " + date)
                    print(Bot + "today's date is : " + date + "\n")
                    engine.runAndWait()

                elif comms in frequest[2]:
                        engine.say("The day today is " + day)
                        print(Bot + "The day today is - " + day + "\n")
                        engine.runAndWait()
                    
                elif (comms in closing) or (comms in byes):                                              # Commands to Exit program
                    rand_byes = random.choice(byes)
                    engine.say(rand_byes)
                    print(Bot + rand_byes.capitalize() + "...\n")
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
                            print searchstr
                            try:
                                wiki_search = ("https://en.wikipedia.org/wiki/" + searchstr)
                                page = urllib2.urlopen(wiki_search)
                                soup = BeautifulSoup(page, "html.parser")

                                post_title = soup.find('h1', {'class' : 'firstHeading'})
                                print ("\n" + post_title.text + ":-")
                                engine.say(post_title.text)
                                definition = soup.find('p')
                                print("\t" + definition.text + "\n")
                                engine.say(definition.text)
                            
                            except:
                                engine.say("Couldn't find "  + comms)
                                print ("Couldn't find "  + comms + "...\n")
                                engine.runAndWait()

                    except:
                        print ('Sorry, couldn\'t understand that...\nPlease try again...')

                elif 'calculate' in comms:                                                                                                                              # 'Calculate' for calculating arithmetic operations
                    commlist = comms.split()
                    try:
                        if (commlist[2]=='+') or (commlist[2]=='subtracted') or (commlist[2]=='added') or (commlist[2]=='times') or (commlist[2]=='multiplied') or (commlist[2]=='divided') or (commlist[2]=='into') or (commlist[2]=='upon') or (commlist[2]=='minus') or (commlist[2]=='by') or (commlist[2]=='x') or (commlist[2]=='-') or (commlist[2]=='/'):
                            global opr
                            opr = commlist[2]
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
                        print ('Sorry, couldn\'t understand that...\nPlease try again...')
                        
                else:
                    print(Bot + "You said : '" + comms + "'\n")
                    
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
            print("Oops! Couldn't get that...\n")
            
        except sr.RequestError as e:
            engine.say("Sorry, can't process at this time... Check your internet connection...")
            engine.say("Terminating this program...")
            print("Sorry, can't process at this time... Check your internet connection...\nTerminating the program...\n")
            engine.runAndWait()
            sys.exit()

except KeyboardInterrupt:
    pass

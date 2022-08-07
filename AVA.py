import json
import os
import random
import re
import string
import sys
import time
import webbrowser
import pyautogui
import pyttsx3
import requests
import speech_recognition as sr
import vlc
from datetime import datetime
from bs4 import *


class ava:
    def __init__(self):
        # Properties and objects for various modules :-
        self.botname = "Jarvis"

        self.engine = pyttsx3.init()
        rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', rate - 30)

        self.opr = None
        self.playMFile = None

        self.mic_recog = sr.Recognizer()
        self.mic = sr.Microphone()

        # Checking lists and dictionaries:-
        self.conjunctions = ['For', 'And', 'Nor', 'But', 'Or', 'Yet', 'So', 'After', 'Although', 'As', 'Because',
                             'Before', 'If', 'Once', 'Since', 'Though', 'Unless', 'Until', 'When', 'Where', 'While']
        self.prepositions = ['About', 'Above', 'Across', 'After', 'Against', 'Along', 'Amid', 'Among', 'Around', 'At',
                             'Before', 'Behind', 'Below', 'Beneath', 'Beside', 'Besides', 'Between', 'Beyond', 'By',
                             'Down', 'In', 'Inside', 'Into', 'Near', 'Of', 'Off', 'On', 'Onto', 'Opposite', 'Outside',
                             'Over', 'Past', 'To', 'Toward', 'Towards', 'Under', 'Underneath', 'Until', 'Up', 'Upon',
                             'Versus', 'Via', 'With', 'Within']
        self.articles = ['A', 'An', 'The']
        self.specialChars = {'hyphen': '-', 'Dash': '-', 'dot': '.', 'full stop': '.', 'comma': ',',
                             'exclamation mark': '!', 'forward slash': '/', 'backslash': '\\', 'backward slash': '\\',
                             'at the rate': '@', 'hash': '#', 'dollar sign': '$', 'percent sign': '%', 'caret': '^',
                             'circumflex': '^', 'ampercent': '&', 'and sign': '&', 'Asterisk': '*', 'asterisk': '*',
                             'parentheses open': '(', 'parentheses close': ')', 'parentheses': '()',
                             'round bracket open': '(', 'round bracket close': ')', 'plus sign': '+',
                             'vertical bar': '|', 'pipe sign': '|', 'curly bracket open': '{',
                             'curly bracket close': '}', 'square bracket open': '[', 'square bracket close': ']',
                             'angle bracket open': '<', 'angle bracket close': '>', 'question mark': '?', 'tilde': '~',
                             'grave sign': '`', 'double inverted quotes': '"', 'double inverted comma': '"',
                             'inverted quotes': "'", 'inverted comma': "'", 'single inverted quotes': "'",
                             'single inverted comma': "'", 'colon': ':', 'semicolon': ';'}
        self.mExtTypes = [['.mp3', '.wav', '.wma', '.m4a', '.xspf'],
                          ['.mp4', '.mkv', '.avi', '.webm', '.3gp', '.gif', '.wmv', '.mov', '.vob', '.flv']]
        self.web_search_prepositions = ['of', 'de']

        # Conversation lists :-
        self.greets = ['hi', 'hello', 'hello there', 'hi there', 'hey', 'hey there', 'namaste', 'hola', 'Howdy']
        self.greets2 = [f'hey {self.botname}', f'hi {self.botname}', f'hello {self.botname}']
        # Questions / Queries -
        self.toggleListening = [
            ['start listening', f'listen {self.botname}', f'{self.botname} listen', f'start listening {self.botname}',
             f'{self.botname} start listening', 'resume listening'],
            ['on hold', 'stop listening', f'stop listening {self.botname}', f'{self.botname} stop listening',
             'pause listening']]
        self.helpcom = ['show all commands', 'show help', 'help', 'show commands', 'show help commands', 'all commands']
        self.info = ['summarize the project', 'project summary', 'tell me something about you in details',
                     'details about you', 'your project summary', 'project summary and details', 'project details']
        self.closing = ['terminate conversation', 'terminate now', 'exit chat', 'exit now', 'terminate', 'close chat',
                        'close conversation', 'close yourself', 'exit conversation', 'end now', 'end chat',
                        'end conversation']
        self.botcall = ['how is everything', 'how are you', 'how are you doing', 'how is everything going on',
                        "what's up"]
        self.frequest = [
            ['what is the time right now', "what's the time right now", 'what time is it right now', "what's the time",
             'what time is it in the clock', 'what is the time', "what's the time now", 'what time is it now',
             'tell me the time'],
            ["what's the date today", 'what is the date today', "today's date is", "tell me today's date",
             "today's date is"],
            ["what is today's day", "what's today's day", 'what is the day today', "today's day is",
             "tell me today's day"]]
        self.readycheck = ['you there', 'are you there', 'are you ready', 'you ready']
        self.botintro = ['who are you', "what's your name", 'who am I talking to', 'what are you', 'what is your name',
                         'what are you called', 'what do people call you']
        self.weatherRep = ['how is the weather today', 'current weather conditions', 'how is the weather',
                           'weather conditions', 'weather forecast']
        self.typeMode = ['typing mode on', 'typing mode off']
        self.whereAbouts = ['where am I', 'what is my location', 'what is my current location', "what's my location",
                            "what's my current location", 'get my location', 'what is this place']
        self.mPlayerToggle = [['play', 'start playing', 'resume playing', 'play that', 'play media'],
                              ['pause', 'hold it', 'pause media', 'pause that'],
                              ['stop', 'stop playing', 'stop media', 'close media']]
        self.mMediaType = [['song', 'music'], ['video', 'visual'], ['movie', 'film']]
        self.automateKBoard = [
            ['close', 'close that', 'close the program', 'close active window', 'close this program', 'close this'],
            ['new tab', 'open new tab', 'start new tab', 'open in new tab', 'make new tab', 'start in new tab'],
            ['enter', 'press enter', 'press return', 'type enter', 'type return', 'press enter button',
             'press return button', 'press enter key', 'press return key', 'enter key'],
            ['press right enter', 'right enter', 'press right enter button', 'press right return',
             'press right return button', 'right enter key', 'press right enter key', 'press right return key',
             'right return key'],
            ['backspace', 'press backspace', 'press backspace button', 'type backspace', 'backspace key',
             'press backspace key'],
            ['delete', 'delete key', 'press delete key', 'press delete', 'press delete button'],
            ['tab', 'tab key', 'tab button', 'press tab key', 'press tab button', 'press tab'],
            ['shift', 'left shift', 'press left shift', 'left shift key', 'press left shift key',
             'press left shift button', 'press shift', 'press shift key', 'press shift button', 'left shift button'],
            ['right shift', 'right shift key', 'right shift button', 'press right shift key',
             'press right shift button'],
            ['caps lock', 'press caps lock', 'caps lock key', 'caps lock button', 'press caps lock key',
             'press caps lock button'],
            ['num lock', 'press num lock', 'num lock key', 'num lock button', 'press num lock key',
             'press num lock button'],
            ['control', 'left control', 'control button', 'control key', 'left control key', 'left control button',
             'press control key', 'press control button', 'press left control key', 'press left control button'],
            ['alter', 'left alter', 'press left alter', 'press alter', 'alter key', 'left alter key', 'alter button',
             'left alter button', 'press alter key', 'press alter button', 'press left alter key',
             'press left alter button'],
            ['right alter', 'right alter key', 'right alter button', 'press right alter', 'press right alter key',
             'press right alter button'],
            ['right control', 'right control key', 'right control button', 'press right control',
             'press right control key', 'press right control button'],
            ['escape', 'press escape', 'escape key', 'escape button', 'press escape key', 'press escape button'],
            ['page up', 'page up key', 'scroll down', 'scroll right', 'page up button', 'press page up',
             'press page up key', 'press page up button'],
            ['page down', 'page down key', 'scroll up', 'scroll left', 'page down button', 'press page down',
             'press page down key', 'press page down button'],
            ['space', 'space bar', 'space bar key', 'space bar button', 'press space bar', 'press space bar key',
             'press space bar button'],
            ['screenshot', 'new screenshot', 'take screenshot', 'create screenshot', 'click a screenshot',
             'get screenshot', 'get a screenshot', 'click screenshot']]

        # self.botname Replies -
        self.botans = ['I am fine...', 'I am doing great...', "I'm fine, thank you...",
                       'I am glad you asked, thank you...', 'Everything is good... thank you...',
                       'Everything is great...', 'Everything Seems good...']
        self.compos = ['At your service', 'Ask me', 'Waiting for your command', 'Tell me something to do',
                       'How can I help you?']
        self.byes = ['until next time', 'bye bye', 'see you soon', 'ciao', 'goodbye', 'catch you later',
                     'see you next time', 'see you later', 'ciao']
        self.introans = [f'I am {self.botname}, your virtual personal assistant', f'They call me "{self.botname}"',
                         f'People call me "{self.botname}"', f'My name is {self.botname}']
        self.readyans = ['I am online and ready...', 'Ready', 'Up and running...', 'Always ready to help and assist...']
        self.projectDetails = "AVA (Accessibility Virtual Assistant) is a virtual assistant developed for better accessiblity and interactivity in an open source environment. This vitual assistant is used to perform some regular tasks like - Getting Date, Time or Day, Simple arithmetic calculations, and Even searching almost anything on internet. These tasks can be performed just by using some voice commands. The project is developed in python."
        self.webSearch = ['found something...', 'This is what I found...', 'Here is what I found on the Internet...',
                          'Here is what I found...', 'Found something...', 'I got this on the Internet...']

        self.date = datetime.now().strftime("%d-%B-%Y")
        self.day = datetime.now().strftime("%A")

    # All Functions (Declaration and definition) :-
    def botspeak(self, out_text):
        self.engine.say(out_text)
        self.engine.runAndWait()

    # Listener toggle -
    def listenToggle(self,
                     command):  # Function to toggle the 'listening' of the program (from 'listening' to 'not listening' or vice versa)
        if command in self.toggleListening[1]:
            while True:
                with self.mic as source:
                    audio = self.mic_recog.listen(source)
                    try:
                        value = self.mic_recog.recognize_google(audio)
                        if str is bytes:
                            toggleCommand = ("{}".format(value).encode("utf-8"))

                            if toggleCommand in self.toggleListening[0]:
                                break

                        else:
                            toggleCommand = ("{}".format(value))

                            if toggleCommand in self.toggleListening[0]:
                                break

                    except sr.UnknownValueError:
                        print("Couldn't understand that...")

    # Play Multimedia -
    # Function to handle multimedia files - Songs, Videos or Movies From predefined paths
    def playMedia(self, mName, mFilePath):
        mediaFilePath = None
        for root, dirs, files in os.walk(mFilePath):
            if mediaFilePath:
                break
            for fileFound in files:
                curFile = re.sub('\s+', ' ', re.sub('[^A-Za-z0-9.\s\']', ' ', fileFound))
                if mName.lower() in curFile.lower():
                    mFileExt = os.path.splitext(fileFound)
                    if mFileExt[1] in self.mExtTypes[0]:
                        mediaFilePath = os.path.join(root, fileFound)
                        break
        return mediaFilePath

    # multimedia state toggle -
    def mMediaToggle(self,
                     command):  # Function for toggling operations, i.e. Play, Pause or Stop the current multimedia file
        if command in self.mPlayerToggle[0]:
            try:
                self.playMFile.play()
            except:
                print("Playing media operation can not be performed")
        elif command in self.mPlayerToggle[1]:
            try:
                self.playMFile.pause()
            except:
                print("Pausing media operation can not be performed !")
        elif command in self.mPlayerToggle[2]:
            try:
                self.playMFile.stop()
            except:
                print("Stopping media operation can not be performed !")

    # Toggle Typing mode -
    def getTypeData(self):  # Function to start the 'Typing Mode'
        self.botspeak("Typing mode is turned on...")

        while True:
            with self.mic as source:
                audio = self.mic_recog.listen(source)
            try:
                value = self.mic_recog.recognize_google(audio)

                if str is bytes:
                    typeData = ("{}".format(value).encode("utf-8"))
                    if typeData == self.typeMode[1]:
                        break
                    elif any(typeData in subl for subl in self.automateKBoard):
                        self.keyBoardAutomater(typeData)
                    elif typeData in self.specialChars:
                        pyautogui.typewrite(typeData)
                    else:
                        pyautogui.typewrite((typeData), interval=0.05)

                else:
                    typeData = ("{}".format(value))
                    if typeData == self.typeMode[1]:
                        break
                    elif any(typeData in subl for subl in self.automateKBoard):
                        self.keyBoardAutomater(typeData)
                    elif typeData in self.specialChars:
                        pyautogui.typewrite(typeData)
                    else:
                        pyautogui.typewrite(typeData, interval=0.05)

            except sr.UnknownValueError:
                self.botspeak("Please repeat !")

        self.botspeak("Typing mode is turned off ")

    # active window operations:-
    def keyBoardAutomater(self,
                          inputCommand):  # Function to automate small windows operations - Closing any current program, Opening a new tab or starting 'typing mode'
        if inputCommand in self.automateKBoard[0]:
            pyautogui.hotkey('altleft', 'f4')
        elif inputCommand in self.automateKBoard[1]:
            pyautogui.hotkey('ctrlleft', 't')
        elif (inputCommand in self.automateKBoard[2]) or (inputCommand in self.automateKBoard[3]):
            pyautogui.hotkey('enter')
        elif inputCommand in self.automateKBoard[4]:
            pyautogui.hotkey('backspace')
        elif inputCommand in self.automateKBoard[5]:
            pyautogui.hotkey('delete')
        elif inputCommand in self.automateKBoard[6]:
            pyautogui.hotkey('tab')
        elif inputCommand in self.automateKBoard[7]:
            pyautogui.hotkey('shiftleft')
        elif inputCommand in self.automateKBoard[8]:
            pyautogui.hotkey('shiftright')
        elif inputCommand in self.automateKBoard[9]:
            pyautogui.hotkey('capslock')
        elif inputCommand in self.automateKBoard[10]:
            pyautogui.hotkey('numlock')
        elif inputCommand in self.automateKBoard[11]:
            pyautogui.hotkey('ctrlleft')
        elif inputCommand in self.automateKBoard[12]:
            pyautogui.hotkey('altleft')
        elif inputCommand in self.automateKBoard[13]:
            pyautogui.hotkey('altright')
        elif inputCommand in self.automateKBoard[14]:
            pyautogui.hotkey('ctrlright')
        elif inputCommand in self.automateKBoard[15]:
            pyautogui.hotkey('escape')
        elif inputCommand in self.automateKBoard[16]:
            pyautogui.hotkey('pgup')
        elif inputCommand in self.automateKBoard[17]:
            pyautogui.hotkey('pgdn')
        elif inputCommand in self.automateKBoard[18]:
            pyautogui.hotkey('space')
        elif inputCommand in self.automateKBoard[19]:
            pyautogui.hotkey('win', 'prtscr')
        elif inputCommand == self.typeMode[0]:
            self.getTypeData()

    # GetLocale:-
    def getLoc(
            self):  # Function to automatically determining the geographic location of the user based on the assigned IP address
        # Automatically geolocate the connecting IP
        f = requests.get('http://ip-api.com/json/')
        json_string = f.text
        f.close()
        location = json.loads(json_string)
        location_city = location['city']
        location_state = location['regionName']
        location_country = location['country']
        location_zip = location['zip']
        reply = "Your current location is : %s, %s, %s." % (location_city, location_state, location_country)
        self.botspeak(reply)
        print(self.botname + " : " + reply + "\n")

    # Weather conditions based on current location :-
    def getLocalWeather(
            self):  # Function to gather local weather (temperature) information based on the autolocated geographic location.
        # Automatically geolocate the connecting IP
        f = requests.get('http://ip-api.com/json/')
        json_string = f.text
        f.close()
        location = json.loads(json_string)
        location_city = location['city']
        location_state = location['regionName']
        location_country = location['country']
        location_zip = location['zip']

        # Get weather conditions at location fetched from above
        f = requests.get(
            "http://api.wunderground.com/api/73a91fc9316a85f8/geolookup/conditions/q/" + location_country + "/" + location_city + ".json")
        json_string = f.text
        parsed_json = json.loads(json_string)
        location = parsed_json['location']['city']
        temp_c = parsed_json['current_observation']['temp_c']
        weatherType = parsed_json['current_observation']['weather']
        degSym = u'\xb0'
        reply = ("Current temperature in %s is: %s " + degSym + "C, with %s weather.") % (location, temp_c, weatherType)
        self.botspeak(reply)
        print(self.botname + " : " + reply + "\n")
        f.close()

    def timing(self):
        reply = ("Current time is " + str(datetime.strftime(datetime.now(), "%I:%M:%S %p")))
        self.botspeak(reply)
        print(self.botname + " :\nTime is : " + reply + "\n")

    # Main program body :-
    def ava(self):
        try:
            while True:
                quest = random.choice(self.compos)
                self.botspeak(quest)
                print("\n\n" + quest + " : \n")

                with self.mic as source:
                    self.mic_recog.adjust_for_ambient_noise(source)
                    audio = self.mic_recog.listen(source)
                print("Processing...")

                try:
                    value = self.mic_recog.recognize_google(audio)
                    comms = ("{}".format(value))
                    print("You -> " + comms)
                    # Starts checking for the reply from here
                    if comms in self.greets or comms in self.greets2:  # If Command was a greeting
                        reply = random.choice(self.greets)
                        self.botspeak(reply)
                        print(self.botname + " : " + reply.capitalize() + "!\n")

                    elif comms in self.info:
                        reply = self.projectDetails
                        self.botspeak(reply)
                        print(self.botname + " : " + reply + "\n")

                    elif comms in self.helpcom:  # If command was to list all available commands
                        reply = "Following commands are stored for interaction and usage right now..."
                        self.botspeak(reply)
                        print(self.botname + " : " + reply + "\n")

                        print("Greeting commands -\n")
                        for i in range(8):
                            reply = self.greets[i]
                            print("\t-> " + reply + "\n")

                        for i in range(3):
                            reply = self.greets2[i]
                            print("\t-> " + reply + "\n")

                        print("\nIntroductory commands -\n")
                        for i in range(7):
                            reply = self.botintro[i]
                            print("\t-> " + reply + "\n")

                        print("\nClosing commands -\n")
                        for i in range(12):
                            reply = self.closing[i]
                            print("\t-> " + reply + "\n")

                        print("\nInteraction commands -\n")
                        for i in range(5):
                            reply = self.botcall[i]
                            print("\t-> " + reply + "\n")

                        for i in range(9):
                            reply = self.readycheck[i]
                            print("\t-> " + reply + "\n")

                        print("\nTime, Date and Day commands -\n")
                        for i in range(9):
                            reply = self.frequest[0][i]
                            print("\t-> " + reply + "\n")

                        for i in range(5):
                            reply = self.frequest[1][i]
                            print("\t-> " + reply + "\n")

                        for i in range(5):
                            reply = self.frequest[2][i]
                            print("\t-> " + reply + "\n")

                        print("\n Project info commands -\n")
                        for i in range(6):
                            reply = self.info[i]
                            print("\t->" + reply + "\n")

                        print("\n##### END OF COMMANDS #####\n")

                    elif comms in self.botintro:  # Commands for bot intro
                        reply = random.choice(self.introans)
                        self.botspeak(reply)
                        print(self.botname + " : " + reply)

                    elif comms in self.botcall:  # Interactive commands
                        reply = random.choice(self.botans)
                        self.botspeak(reply)
                        print(self.botname + " : " + reply)

                    elif comms in self.readycheck:  # Interactive commands
                        reply = random.choice(self.readyans)
                        self.botspeak(reply)
                        print(self.botname + " : " + reply)

                    elif comms in self.frequest[0]:  # Commands to know - Time, Date or Day.
                        self.timing()

                    elif comms in self.frequest[1]:
                        reply = self.date
                        self.botspeak("Today's date is " + reply)
                        print(self.botname + " : " + "today's date is : " + reply + "\n")

                    elif comms in self.frequest[2]:
                        reply = self.day
                        self.botspeak("The day today is : " + reply)
                        print(self.botname + " : " + "The day today is - " + reply + "\n")

                    elif comms in self.toggleListening[1]:
                        self.listenToggle(comms)

                    elif comms in self.weatherRep:  # Command to get 'weather' information for current location of execution
                        self.getLocalWeather()

                    elif (comms in self.automateKBoard) or (
                            comms in self.typeMode):  # Automate keyboard keys and shortcuts
                        self.keyBoardAutomater(comms)

                    elif comms in self.whereAbouts:  # Automatically locate the location of execution
                        self.getLoc()

                    elif (comms in self.mPlayerToggle[0]) or (comms in self.mPlayerToggle[1]) or (
                            comms in self.mPlayerToggle[2]):
                        self.mMediaToggle(comms)

                    elif comms.startswith(
                            'play'):  # Condition for playing or starting a multimedia file (Song/Video/Music)
                        mTypeGetter = comms.split()
                        mPath = ''
                        if (mTypeGetter[0] == 'play') and (mTypeGetter[1] in self.mMediaType[0]):
                            mPath = 'C:/Users/Lenovo/Music/'
                        elif (mTypeGetter[0] == 'play') and (mTypeGetter[1] in self.mMediaType[1]):
                            mPath = 'C:/Users/lenovo/Videos/'
                        elif (mTypeGetter[0] == 'play') and (mTypeGetter[1] in self.mMediaType[2]):
                            mPath = 'D:/Movies/'
                        for remIndex in range(2):
                            mTypeGetter.remove(mTypeGetter[0])
                        mTypeGetter = " ".join(mTypeGetter)
                        mFilename = mTypeGetter
                        mediaFilePath = self.playMedia(mFilename, mPath)

                        if mediaFilePath:
                            try:
                                self.playMFile = vlc.MediaPlayer(mediaFilePath)
                                self.playMFile.play()
                            except:
                                print(f"Exception in playing media file: {mediaFilePath}")
                        else:
                            print('File not found!')

                    # Commands to Exit program
                    elif (comms in self.closing) or (comms in self.byes):
                        reply = random.choice(self.byes)
                        self.botspeak(reply)

                        print(self.botname + " : " + reply.capitalize() + "...\n")
                        sys.exit()

                    # Use 'Search', 'Search For', 'Define', 'who is' or 'what is' to find any definition online.
                    elif ('search' in comms) or ('search' and 'for' in comms) or ('define' in comms) or (
                            ('what' and 'is') in comms) or (('who' and 'is') in comms):
                        try:
                            commlist = string.capwords(comms).split()
                            found_prepo = False
                            for prepo in self.web_search_prepositions:
                                if found_prepo:
                                    break
                                for idx, val in enumerate(commlist):
                                    if prepo.capitalize() == val:
                                        commlist[idx] = prepo.lower()
                                        found_prepo = True
                                        break

                            listlen = len(commlist)
                            if (((commlist[0] == 'Define') or (commlist[0] == 'Search')) and (listlen <= 1)) or (((
                                                                                                                          commlist[
                                                                                                                              0] == 'What' and
                                                                                                                          commlist[
                                                                                                                              1] == 'Is') or (
                                                                                                                          commlist[
                                                                                                                              0] == 'Who' and
                                                                                                                          commlist[
                                                                                                                              1] == 'Is') or (
                                                                                                                          commlist[
                                                                                                                              0] == 'Search' and
                                                                                                                          commlist[
                                                                                                                              1] == 'For')) and (
                                                                                                                         listlen <= 2)):
                                raise

                            elif (commlist[0] == 'Define') or (commlist[0] == 'Search') or (
                                    commlist[0] == 'Search' and commlist[1] == 'For') or (
                                    commlist[0] == 'What' and commlist[1] == 'Is') or (
                                    commlist[0] == 'Who' and commlist[1] == 'Is') or (
                                    commlist[0] == 'Who' and commlist[1] == 'Are'):
                                for x in range(listlen - 1):
                                    if (commlist[x] in self.conjunctions) or (commlist[x] in self.prepositions) or (
                                            commlist[x] in self.articles):
                                        commlist[x] = commlist[x].lower()

                                if commlist[0] == 'Define':
                                    commlist.remove('Define')
                                elif commlist[0] == 'Search' and commlist[1] == 'for':
                                    commlist.remove('Search')
                                    commlist.remove('for')
                                elif commlist[0] == 'Search':
                                    commlist.remove('Search')
                                elif commlist[0] == 'What' and commlist[1] == 'Is':
                                    commlist.remove('What')
                                    commlist.remove('Is')
                                elif commlist[0] == 'Who' and commlist[1] == 'Is':
                                    commlist.remove('Who')
                                    commlist.remove('Is')
                                elif commlist[0] == 'Who' and commlist[1] == 'Are':
                                    commlist.remove('Who')
                                    commlist.remove('Are')

                                try:
                                    searchstr = "_".join(commlist)
                                    wiki_search = "https://en.wikipedia.org/wiki/" + searchstr
                                    page = requests.get(wiki_search).text
                                    soup = BeautifulSoup(page, "html.parser")
                                    html = soup.find('div', {'id': 'bodyContent'})
                                    paras = html.findAll('p')
                                    reply = ""
                                    for para in paras:
                                        if para.text.strip() != "":
                                            reply = para.text.strip()
                                            if 'refers to:' not in reply.lower():
                                                break
                                    print("\n" + searchstr + ":-")
                                    print("\t" + reply + "\n")
                                    self.botspeak(reply)

                                except:
                                    searchstr = commlist
                                    search = random.choice(self.webSearch)
                                    concSay = " ".join(searchstr)
                                    self.botspeak(search + " about " + concSay)
                                    searchstr = "+".join(searchstr)
                                    webbrowser.open('http://www.google.com/search?q=' + searchstr)
                        except:
                            raise

                    # 'Calculate' for calculating arithmetic operations
                    elif 'calculate' in comms:
                        commlist = comms.split()
                        try:
                            if (commlist[2] == '+') or (commlist[2] == 'subtracted') or (commlist[2] == 'added') or (
                                    commlist[2] == 'times') or (commlist[2] == 'multiplied') or (
                                    commlist[2] == 'divided') or (commlist[2] == 'into') or (commlist[2] == 'upon') or (
                                    commlist[2] == 'minus') or (commlist[2] == 'by') or (commlist[2] == 'x') or (
                                    commlist[2] == '-') or (commlist[2] == '/'):
                                opr = commlist[2]

                                # Basic arithmetic calculations -
                                def calc():
                                    if (opr == '+') or (opr == 'added') or (opr == 'plus'):
                                        res = num1 + num2
                                        n1 = str(num1)
                                        n2 = str(num2)
                                        sol = str(res)
                                        reply = ('The sum would be ' + sol)
                                        self.botspeak(reply)
                                        print(self.botname + " : " + n1 + ' + ' + n2 + ' = ' + sol + "\n")

                                    elif (opr == '-') or (opr == 'minus') or (opr == 'subtracted'):
                                        res = num1 - num2
                                        n1 = str(num1)
                                        n2 = str(num2)
                                        sol = str(res)
                                        reply = ('The difference would be ' + sol)
                                        self.botspeak(reply)
                                        print(self.botname + " : " + n1 + ' - ' + n2 + ' = ' + sol + "\n")

                                    elif (opr == 'x') or (opr == 'into') or (opr == 'multiplied') or (opr == 'times'):
                                        res = num1 * num2
                                        n1 = str(num1)
                                        n2 = str(num2)
                                        sol = str(res)
                                        reply = ('The product would be ' + sol)
                                        self.botspeak(reply)
                                        print(self.botname + " : " + n1 + ' x ' + n2 + ' = ' + sol + "\n")

                                    elif (opr == '/') or (opr == 'divided') or (opr == 'upon') or (opr == 'by'):
                                        res = num1 / num2
                                        n1 = str(num1)
                                        n2 = str(num2)
                                        sol = str(res)
                                        reply = ('The result of division would be ' + sol)
                                        self.botspeak(reply)
                                        print(self.botname + " : " + n1 + ' / ' + n2 + ' = ' + sol + "\n")

                                    else:
                                        reply = "Only four basic arithmetic operations allowed right now..."
                                        self.botspeak(reply)
                                        print(reply + "\n")

                                if (commlist[3] == 'to') or (commlist[3] == 'by') or (commlist[3] == 'with'):
                                    oprprep = commlist[3]
                                    num1 = float(commlist[1])
                                    num2 = float(commlist[4])
                                    calc()
                                else:
                                    num1 = float(commlist[1])
                                    num2 = float(commlist[3])
                                    calc()

                        except:
                            print('Sorry, couldn\'t understand that...\nPlease try again...')

                    else:
                        print(self.botname + " =>\n" + "You said : '" + comms + "'\n")

                except sr.UnknownValueError:
                    print('Sorry, couldn\'t understand that... \nPlease try again...')

                except sr.RequestError:
                    reply = "Sorry, can't process at this time... \nCheck your internet connection...\n\nTerminating the program...\n"
                    self.botspeak(reply)
                    print(reply)
                    sys.exit()

        except KeyboardInterrupt:
            pass


if __name__ == "__main__":
    obj = ava()
    obj.ava()

"""
    Author - Harshawardhan Natu
    Python - Python 3
"""

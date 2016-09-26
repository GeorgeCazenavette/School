# Code is strictly for the GUI
import RPi.GPIO as GPIO
from Tkinter import *
from time import time, sleep, strftime, localtime
import random, csv
import threading
from twilio.rest import TwilioRestClient
import smtplib


changing = False
safetyPin = 6
relayPin = 12
GPIO.setmode(GPIO.BCM)
GPIO.setup(safetyPin, GPIO.OUT)
GPIO.setup(relayPin, GPIO.OUT)

GPIO.output(safetyPin, 0)
GPIO.output(relayPin, 0)

mode = "idle"
authCode = ""
timeToWait = 0
waitingSince = 0

# placeholder
sentCode = "123456"


with open('timeAuthCodeGenerated.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            lastRequestTime = row[0]
            break
print lastRequestTime.split("$")[0], lastRequestTime.split("$")[1]
    
 
class GUITest(Frame):
    def __init__(self, master):
        #master.minsize(width=1280, height=720)
        #master.maxsize(width=1280, height=720)        
        Frame.__init__(self, master)
        self.master = master
        for i in range(5):
            master.grid_columnconfigure(i, weight=1, uniform="group")
        for i in range(5):
            master.grid_rowconfigure(i, weight=1, uniform="group")
    
    def setupGUI(self):
        
        self.printedCode = Label(self.master, text = userInput, font = ("Helvetica", 32), bg = "white")
        self.printedCode.grid(row=0,column=0, columnspan = 3, sticky = NSEW)

        number1 = Button(self.master, text='1', font = ("Helvetica", 32), command = add1, fg = "#000080")
        number1.grid(row=1, column=0, sticky = NSEW)
        
        number2 = Button(self.master, text='2', font = ("Helvetica", 32), command = add2, fg = "#000080")
        number2.grid(row=1, column=1, sticky = NSEW)
        
        number3 = Button(self.master, text='3', font = ("Helvetica", 32), command = add3, fg = "#000080")
        number3.grid(row=1, column=2, sticky = NSEW)
        
        number4 = Button(self.master, text='4', font = ("Helvetica", 32), command = add4, fg = "#000080")
        number4.grid(row=2, column=0, sticky = NSEW)
        
        number5 = Button(self.master, text='5', font = ("Helvetica", 32), command = add5, fg = "#000080")
        number5.grid(row=2, column=1, sticky = NSEW)
        
        number6 = Button(self.master, text='6', font = ("Helvetica", 32), command = add6, fg = "#000080")
        number6.grid(row=2, column=2, sticky = NSEW)
        
        number7 = Button(self.master, text='7', font = ("Helvetica", 32), command = add7, fg = "#000080")
        number7.grid(row=3, column=0, sticky = NSEW)
        
        number8 = Button(self.master, text='8', font = ("Helvetica", 32), command = add8, fg = "#000080")
        number8.grid(row=3, column=1, sticky = NSEW)
        
        number9 = Button(self.master, text='9', font = ("Helvetica", 32), command = add9, fg = "#000080")
        number9.grid(row=3, column=2, sticky = NSEW)
        
        number0 = Button(self.master, text='0', font = ("Helvetica", 32), command = add0, fg = "#000080")
        number0.grid(row=4, column=1, sticky = NSEW)

        backArrow = Button(self.master, text='←', font = ("Helvetica", 32), command = backSpace, fg = "red")
        backArrow.grid(row=4, column=0, sticky = NSEW)

        checkMark = Button(self.master, text='✓', font = ("Helvetica", 32), command = verifyAuthCode, fg = "green")
        checkMark.grid(row=4, column=2, sticky = NSEW)

        SMS = Button(self.master, text = "SEND CODE\nVIA TEXT", font = ("Helvetica", 24), command = SMSCode)
        SMS.grid(row=3, column=3, rowspan=1, columnspan=2, sticky = NSEW)

        call = Button(self.master, text = "SEND CODE\nVIA CALL", font = ("Helvetica", 24), command = callCode)
        call.grid(row=4, column=3, rowspan=1, columnspan=2, sticky = NSEW)

        newNumber = Button(self.master, text = "Change Associated\nPhone Number", font = ("Helvetica", 24), command = changePhone)
        newNumber.grid(row=2, column=3, rowspan=1, columnspan=2, sticky = NSEW)

        self.instructions = Label(self.master, text = "Welcome to AutoBox!", font = ("Helvetica", 24), bg = "#808080", width = 20)
        self.instructions.grid(row=0, column=3, rowspan=1, columnspan=2, sticky = NSEW)

        self.lastRequestLabel= Label(self.master, text = "Last Request @\n%s\n%s" %(lastRequestTime.split("$")[0], lastRequestTime.split("$")[1]), font = ("Helvetica", 24), bg = "#00bfff")
        self.lastRequestLabel.grid(row=1, column=3, rowspan=1, columnspan=2, sticky = NSEW)
        

def add1():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "1"
        t.printedCode.config(text = userInput)
        print userInput

def add2():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "2"
        t.printedCode.config(text = userInput)
        print userInput

def add3():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "3"
        t.printedCode.config(text = userInput)
        print userInput

def add4():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "4"
        t.printedCode.config(text = userInput)
        print userInput

def add5():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "5"
        t.printedCode.config(text = userInput)
        print userInput

def add6():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "6"
        t.printedCode.config(text = userInput)
        print userInput

def add7():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "7"
        t.printedCode.config(text = userInput)
        print userInput

def add8():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "8"
        t.printedCode.config(text = userInput)
        print userInput

def add9():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "9"
        t.printedCode.config(text = userInput)
        print userInput

def add0():
    global mode
    if (mode == "entering"):
        global userInput
        userInput += "0"
        t.printedCode.config(text = userInput)
        print userInput

def backSpace():
    global mode
    if (mode == "entering"):
        global userInput
        userInput = userInput[:-1]
        t.printedCode.config(text = userInput)
        print userInput

# no longer used
def submitCode():
    global mode
    if (mode == "entering"):
        global userInput
        global sentCode
        if (userInput != sentCode):
            t.printedCode.config(bg = "red", text = userInput)
            t.instructions.config(text = "Incorrect Passcode\nYou Must Request a New One")
            #print "should be red?"
            t.update_idletasks()
            sleep(2)
            userInput = ""
            t.printedCode.config(bg = "white", text = userInput)
            mode = "idle"
        else:
            t.printedCode.config(bg = "green")
            t.update_idletasks()
            sleep(1.5)
            userInput = ""
            t.printedCode.config(bg = "white", text = userInput)
            mode = "idle"


def generateAuthCode():
    # generates a random number between these ranges (inclusive)
    global authCode
    global mode
    if (mode == "idle"):
        authCode = ""
        for i in range (6):
            authCode += str( random.randint(0, 9))
        
        
        # store the date and time that the authCode was generated
        timeAuthCodeGenerated = strftime("%m/%d/%Y$%H:%M", localtime())
        
        # write the data to the file
        outputFile = open('timeAuthCodeGenerated.csv', 'w')
        outputWriter = csv.writer(outputFile)
        outputWriter.writerow([timeAuthCodeGenerated])
        outputFile.close()
        t.lastRequestLabel.config(text = "Last Request @\n%s\n%s" %(timeAuthCodeGenerated.split("$")[0], timeAuthCodeGenerated.split("$")[1]))
        return authCode
    
# generateAuthCode()

def verifyAuthCode():

    # get the last authCode from the csv file 
    #with open('timeAuthCodeGenerated.csv', 'r') as f:
     #   reader = csv.reader(f)
      #  for row in reader:
       #     lastRequestAuthCode, lastRequestTime = row
        #    break
        #reader.close()
    
    
    # if lastRequestAuthCode.strip() == str(377127):
    #     print "success"
    # else:
    #     print 'failure'
        
        
    # global userInput
    global authCode
    global userInput
    global mode
    if (mode == "entering"):
        if (authCode != userInput):
            t.printedCode.config(bg = "red", text = userInput)
            t.instructions.config(text = "Incorrect Passcode\nYou Must Request a New One")
            # print "should be red?"
            t.update_idletasks()
            # keep relay off
            GPIO.output(relayPin, 0)
            sleep(1.5)
            userInput = ""
            t.printedCode.config(bg = "white", text = userInput)
            t.instructions.config(text = "Welcome to AutoBox!")
            mode = "idle"
            
            
        else:
            t.printedCode.config(bg = "green")
            if (not changing):
                t.instructions.config(text = "Correct Passcode\nThe Box is Now Unlocked")
                t.update_idletasks()
                # turn on relay
                GPIO.output(relayPin, 1)
                sleep(5)
                GPIO.output(relayPin, 0)
                
            userInput = ""
            t.printedCode.config(bg = "white", text = userInput)
            t.instructions.config(text = "Welcome to AutoBox!")
            mode = "idle"

def SMSCode():

    global mode
    global timeToWait
    global waitingSince
    if (mode == "idle"):
        print "SMS CODE"
        timeToWait = 60
        sendSMSCode(generateAuthCode(), timeToWait)
        t.instructions.config(text = "Code Has Been Sent!")
        t.update_idletasks()
        print "Something else"
        waitingSince = time()
        mode = "entering"
        timerThread = threading.Thread(target=timer)
        print "almost to the thread"
        timerThread.start()
        print "after the thread"

def callCode():
    global mode
    global timeToWait
    global waitingSince
    if (mode == "idle"):
        sendCallCode(generateAuthCode())
        timeToWait = 60
        waitingSince = time()
        mode = "entering"
        timerThread = threading.Thread(target=timer)
        timerThread.start()

def sendSMSCode(code, timeToWait):
   # number to send the code to 
   number = ''
   # message to send the user
   msg = "\nYour one-time Autobox code is: \n%s\nYou have %s seconds to enter it." %(code, timeToWait) 
   
   # setup the connection between the client and the smtp server  
   # instantate an object to interact wih the ser
   server = smtplib.SMTP('smtp.gmail.com', 587)
   # use tls encryption
   server.starttls()
   # login into the server
   server.login("@gmail.com", "")
   # list of phone carriers to iterate over
   listOfCarriers = ['sms.alltelwireless.com',
                  'txt.att.net', 
                  'sms.myboostmobile.com',
                  'mms.cricketwireless.net',
                  'msg.fi.google.com',
                  'text.republicwireless.com',
                  'messaging.sprintpcs.com',
                  'tmomail.net',
                  'email.uscc.net',
                  'vtext.com',
                  'vmobi.com',
                  ]
                  
   # send a message to each potential carrier
   for carrier in listOfCarriers:
      # try to send 
      try:
         server.sendmail('', number+'@'+carrier, msg)
      # if fails, reset the connection
      except:
         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login("", "")
         server.sendmail('.com', number+'@'+carrier, msg)
   
   server.quit()
    

def sendCallCode(x):
    pass

def changePhone():
    global changing
    changing = True
    SMSCode()

def timer():
    
    global mode
    global timeToWait
    global waitingSince
    global userInput
    print ( time() - timeToWait )
    while ((( time() - waitingSince ) < timeToWait ) and mode == "entering"):
        print ( time() - timeToWait )
        #pass
    if (mode == "entering"):
        t.printedCode.config(bg = "red")
        t.instructions.config(text = "Time For This Code Has Expired\nPlease Request a New Code")
        mode = "None"
        t.update_idletasks()
        sleep(4)
        userInput = ""
        t.printedCode.config(bg = "white", text = userInput)
        t.instructions.config(text = "Welcome to AutoBox!")
        mode = "idle"
    


userInput = ""
window = Tk()
window.attributes("-fullscreen",True)
#window.overrideredirect(1)

t = GUITest(window)

t.setupGUI()
#window.resizable(width=FALSE, height=FALSE)



window.mainloop()

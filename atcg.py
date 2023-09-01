import tkinter as tk
from tkinter import ttk, font, messagebox
import random
from time import sleep
from threading import Thread
from tkinter import *
import mysql.connector
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import sys, os 


root = tk.Tk()
#root.geometry("800x700+300+60")
root.title("Clicking Game")
root.state('zoomed')
photo = PhotoImage(file = "click.png")
root.iconbitmap(r"click.ico")
root.iconphoto(False, photo)
root.unbind_all("<Tab>")
root.unbind_all("<<NextWindow>>")
root.unbind_all("<<PrevWindow>>")

xcoord = random.randint(13, 1445)
ycoord = random.randint(70, 770)
daymode = False
nightmode = True
def daymode_f():
    global daymode, nightmode
    daymode = True
    nightmode = False
    home_page()

def nightmode_f():
    global nightmode, daymode
    nightmode = True
    daymode = False
    home_page()

def home_page():
    global daymode, nightmode, connected
    delete_screen()
    frame = tk.Frame(root, bg='black')
    frame.pack(anchor="center", fill="both", expand=True)
    root.configure(bg='black')

    l = tk.Label(frame, text="Select a time", bg="black", fg="white", font=('Helvetica 18 bold', 45))
    #l.grid(row=0, column=0, pady=(50, 0))
    l.pack(pady=(50, 0))
    #l.pack()
    highscore_button = HoverButton(frame, activebackground='#c7c7c7', text="Leaderboard", fg="black", bg="lightgreen", font=('Arial', '16'), width=15, height=0, command=lambda: highscore_page())

    if connected == True:
        #highscore_button.grid(row=0, column=0, pady=(40, 1), padx=(1300, 1))
        highscore_button.pack(pady=(0, 0), padx=(500, 1))
        
    s5 = HoverButton(frame, activebackground='green', text="5 seconds game", fg="black", bg="green", font=('Helvetica', '20'), width=15, height=0, command=lambda: game(5))
    #s5.grid(row=1, column=0, pady=(30, 3), padx=(0, 1))
    s5.pack(pady=(0, 3), padx=(0, 1))

    s10 = HoverButton(frame, activebackground='#c7c7c7', text="10 seconds game", fg="black", bg="green", font=('Helvetica', '20'), width=15, height=0, command=lambda: game(10))
    #s10.grid(row=2, column=0, pady=(0, 3), padx=(0, 1))
    s10.pack(pady=(0, 3), padx=(0, 1))

    s30 = HoverButton(frame, activebackground='#c7c7c7', text="30 seconds game", fg="black", bg="green", font=('Helvetica', '20'), width=15, height=0, command=lambda: game(30))
    #s30.grid(row=3, column=0, pady=(0, 3), padx=(0, 1))
    s30.pack(pady=(0, 3), padx=(0, 1))

    s60 = HoverButton(frame, activebackground='#c7c7c7', text="60 seconds game", fg="black", bg="green", font=('Helvetica', '20'), width=15, height=0, command=lambda: game(60))
    #s60.grid(row=4, column=0, pady=(0, 3), padx=(0, 1))
    s60.pack(pady=(0, 3), padx=(0, 1))
    
    btutorial = HoverButton(frame, activebackground='#c7c7c7', text="Tutorial", fg="black", bg="lightgreen", font=('Arial', '16'), width=15, height=0, command=lambda: tutorial_page())
    #btutorial.grid(row=5, column=0, pady=(10, 1), padx=(0, 1))
    btutorial.pack(pady=(10, 1), padx=(0, 1))



        

    if daymode == True:
        root.configure(bg="SystemButtonFace")
        frame.config(bg="SystemButtonFace")
        l.config(bg="SystemButtonFace", fg="black")
        
        night = HoverButton(root, activebackground='#c7c7c7', text="dark mode", fg="black", bg="grey", width=0, height=0, command=lambda: nightmode_f()).pack(pady=20)
    else:
        day = HoverButton(root, activebackground='#c7c7c7', text="light mode", fg="black", bg="grey", width=0, height=0, command=lambda: daymode_f()).pack(pady=20)



def check_highscore():
    global connection, s5p1, s5p2, s5p3, s10p1, s10p2, s10p3, s30p1, s30p2, s30p3, s60p1, s60p2, s60p3, s5n1, s5n2, s5n3, s10n1, s10n2, s10n3, s30n1, s30n2, s30n3, s60n1, s60n2, s60n3
    sql_select_Query = "select * from highscores_game"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
   #######################################
                                                    #5
    x5 = y5= z5 = False
    s5p1 = s5p2 = s5p3 = 0
    s5n1 = s5n2 = s5n3 = "untaken!"
    s5list = []
    for row in records:
        if row[1] == 5:
            s5list.append(row[3])
    
    s5p3 = min(s5list)
    s5list.remove(s5p3)
    s5p1 = max(s5list)
    s5list.remove(s5p1)         #10 , piet, 0
    s5p2 = s5list[0]            #10, piet, 0

    for row in records:
        if row[1] == 5:
            if row[3] == s5p1 and x5 == False:
                s5n1 = row[2]
                x5 = True
            elif row[3] == s5p2 and y5 == False:
                s5n2 = row[2]
                y5 = True
            elif row[3] == s5p3 and z5 == False:
                s5n3 = row[2]
                z5 = True

   #######################################
                                                    #10
    x10 = y10= z10 = False
    s10p1 = s10p2 = s10p3 = 0
    s10n1 = s10n2 = s10n3 = "untaken!"
    s10list = []
    for row in records:
        if row[1] == 10:
            s10list.append(row[3])
    
    s10p3 = min(s10list)
    s10list.remove(s10p3)
    s10p1 = max(s10list)
    s10list.remove(s10p1)
    s10p2 = s10list[0]

    for row in records:
        if row[1] == 10:
            if row[3] == s10p1 and x10 == False:
                s10n1 = row[2]
                x10 = True
            elif row[3] == s10p2 and y10 == False:
                s10n2 = row[2]
                y10 = True
            elif row[3] == s10p3 and z10 == False:
                s10n3 = row[2]
                z10 = True
                

   #######################################
                                                    #30
    x30 = y30 = z30 = False
    s30p1 = s30p2 = s30p3 = 0
    s30n1 = s30n2 = s30n3 = "untaken!"
    s30list = []
    for row in records:
        if row[1] == 30:
            s30list.append(row[3])
    
    s30p3 = min(s30list)
    s30list.remove(s30p3)
    s30p1 = max(s30list)
    s30list.remove(s30p1)
    s30p2 = s30list[0]

    for row in records:
        if row[1] == 30:
            if row[3] == s30p1 and x30 == False:
                s30n1 = row[2]
                x30 = True
            elif row[3] == s30p2 and y30 == False:
                s30n2 = row[2]
                y30 = True
            elif row[3] == s30p3 and z30 == False:
                s30n3 = row[2]
                z30 = True
                

   #######################################
                                                    # 60
    x60 = y60 = z60 = False
    s60p1 = s60p2 = s60p3 = 0
    s60n1 = s60n2 = s60n3 = "untaken!"
    s60list = []
    for row in records:
        if row[1] == 60:
            s60list.append(row[3])
    
    s60p3 = min(s60list)
    s60list.remove(s60p3)
    s60p1 = max(s60list)
    s60list.remove(s60p1)
    s60p2 = s60list[0]

    for row in records:
        if row[1] == 60:
            if row[3] == s60p1 and x60 == False:
                s60n1 = row[2]
                x60 = True
            elif row[3] == s60p2 and y60 == False:
                s60n2 = row[2]
                y60 = True
            elif row[3] == s60p3 and z60 == False:
                s60n3 = row[2]
                z60 = True

    connection.commit()
    cursor.close()

    
def highscore_page():
    check_highscore()
    #global connection, s5p1, s5p2, s5p3, s10p1, s10p2, s10p3, s30p1, s30p2, s30p3, s60p1, s60p2, s60p3, s5n1, s5n2, s5n3, s10n1, s10n2, s10n3, s30n1, s30n2, s30n3, s60n1, s60n2, s60n3
    delete_screen()
    root.configure(bg="black")
    
    canvas = Canvas(root, height=60, width=400, bg='black', highlightthickness=1, highlightbackground="black")
    canvas.pack(fill=tk.BOTH, expand=True, side=BOTTOM)

    
    
    text1 = '''
 5 seconds:
    1st place: {}
    2nd place: {}
    3rd place: {}

10 seconds:
    1st place: {}
    2nd place: {}
    3rd place: {}
    
30 seconds:
    1st place: {}
    2nd place: {}
    3rd place: {}
    
60 seconds:
    1st place: {}
    2nd place: {}
    3rd place: {}
'''
    text2 = '''

                    with {} points
                    with {} points
                    with {} points


                    with {} points
                    with {} points
                    with {} points
    

                    with {} points
                    with {} points
                    with {} points
    

                    with {} points
                    with {} points
                    with {} points
'''
    canvas.create_text(800, 35,fill="green", anchor='center', font=("Arial CYR", 50), text='HIGHSCORES')

    canvas.create_text(600,400,fill="green", anchor='center', font=("Lucida Console", 22), text=text1.format(s5n1, s5n2, s5n3,
                                                                                                             s10n1, s10n2, s10n3,
                                                                                                             s30n1, s30n2, s30n3,
                                                                                                             s60n1, s60n2, s60n3,))
    canvas.create_text(800,400,fill="green", anchor='center', font=("Lucida Console", 22), text=text2.format(s5p1, s5p2, s5p3,
                                                                                                             s10p1, s10p2, s10p3,
                                                                                                             s30p1, s30p2, s30p3,
                                                                                                             s60p1, s60p2, s60p3,))
    
    home_button = HoverButton(canvas, activebackground='#c7c7c7', text="Main Menu", fg="black", bg="green", font=('Arial', '16'), width=0, height=0, command=lambda: home_page())
    home_button.pack(side=BOTTOM, anchor="sw", padx=15, pady=15)
    

def tutorial_page():
    delete_screen()
    root.configure(bg="black")
    canvas = Canvas(root, height=60, width=400, bg='black', highlightthickness=1, highlightbackground="black")
    canvas.pack(fill=tk.BOTH, expand=1, side=BOTTOM)

    
    
    texts = '''
When you have selected a time/difficulty in the main menu
You will see text saying "Click to start" and a green square.
When you have clicked the green square the timer will start
counting down from the time selected to 0.
Next to the timer you can also see your score
your score is the amount of targets (green squares) you've clicked

your time is over when you see "TIME OVER" in your screen (if you couldn't figure out).
When the time is over, your score will automatically be checked
for a possible new highscore (if a connection to the online database is made).
Your goal is to click as many targets as possible in the time limit and set a new highscore!

Good luck
-Jordy
'''

    canvas.create_text(660,300,fill="green", anchor='center', font=("Arial CYR", 25), text=texts)
    home_button = HoverButton(canvas, activebackground='#c7c7c7', text="Main Menu", fg="black", bg="green", font=('Arial', '16'), width=0, height=0, command=lambda: home_page())
    home_button.pack(side=BOTTOM, anchor="sw", padx=15, pady=15)



def game(time_button):
    global cframe, button, label, score_label, kill, timer_label, daymode, time_countdown
    time_countdown = time_button
    kill = False
    delete_screen()
    tframe = tk.Frame(root)
    tframe.pack(anchor="n")
    label = tk.Label(tframe, text="Click to start!", fg='black', font=10)
    label.grid(row=0, column=0, pady=(15, 0))
    score_label = tk.Label(tframe, text="SCORE: 0", fg='black', font=10)
    timer_label = tk.Label(tframe, text="TIME: 0", fg='black', font=10)

    canvas = tk.Canvas(width=1600, height=14)
    if nightmode == True:
        canvas.create_line(0, 15, 1600, 15, fill='white', width=2)
    else:
        canvas.create_line(0, 15, 1600, 15, fill='grey', width=2)
    canvas.place(x=0, y=40)

    cframe = tk.Frame(root)
    cframe.pack(anchor="center", pady=15)
    cframe.configure(bg="black")

    if nightmode == True:
        tframe.configure(bg="black")
        root.configure(bg='black')
        cframe.configure(bg='black')
        canvas.configure(bg='black', highlightthickness=1, highlightbackground="black")
        score_label.configure(bg='black', fg="white")
        timer_label.configure(bg='black', fg="white")
        label.configure(bg='black', fg="white")
        
    
    button = HoverButton(root, activebackground='#c7c7c7', text="", fg="black", bg="green", font=('Helvetica', '20'), width=4, height=1, command=lambda: click())
    button.pack()


def after_game():
    global xcoord, ycoord, score, score_label, kill, time_countdown
    button.destroy()
    if nightmode == True:
        l = tk.Label(root, text="TIME OVER", fg="white", bg="black", font=('Helvetica', '50'))
        l.pack(pady=150)
    else:
        l = tk.Label(root, text="TIME OVER", font=('Helvetica', '50'))
        l.pack(pady=150)
        
    b = HoverButton(root, activebackground='#c7c7c7', text="Back to main menu", fg="black", bg="green", font=('Helvetica', '20'), width=0, height=0, command=lambda: home_page()).pack()
    pagain = HoverButton(root, activebackground='#c7c7c7', text="Play again", fg="black", bg="green", font=('Helvetica', '20'), width=0, height=0, command=lambda: game(time_countdown)).pack()


    if connected == True:
        check_highscore()
        
        if time_countdown == 5:
            if score > s5p3:
                while True:
                    name = askstring('Highscore!', 'You hit a new highscore!\nWe would like to know your name for the leaderboard!\n(if you press cancel you will not be added to the leaderboard)')
                    if name == None:
                        break
                    elif name == "":
                        print('error')
                        messagebox.showerror("Error", "Name can not be empty!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif name.isspace() == True:
                        messagebox.showerror("Error", "Name can not be spaces only!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif len(name) > 10:
                        messagebox.showerror("Error", "Name can not be longer than 10 characters!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    else:
                        showinfo('Highscore', 'Hi {}, congrats with your score!\nYour score is added to the leaderboard!'.format(name))
                        edit_leaderboard(5, s5p3, name)
                        break
                            

##                        

        elif time_countdown == 10:
            if score > s10p3:
                while True:
                    name = askstring('Highscore!', 'You hit a new highscore!\nWe would like to know your name for the leaderboard!\n(if you press cancel you will not be added to the leaderboard)')
                    if name == None:
                        break
                    elif name == "":
                        print('error')
                        messagebox.showerror("Error", "Name can not be empty!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif name.isspace() == True:
                        messagebox.showerror("Error", "Name can not be spaces only!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif len(name) > 10:
                        messagebox.showerror("Error", "Name can not be longer than 10 characters!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    else:
                        showinfo('Highscore', 'Hi {}, congrats with your score!\nYour score is added to the leaderboard!'.format(name))
                        edit_leaderboard(10, s10p3, name)
                        break
                                                
                        
        elif time_countdown == 30:
            if score > s30p3:
                while True:
                    name = askstring('Highscore!', 'You hit a new highscore!\nWe would like to know your name for the leaderboard!\n(if you press cancel you will not be added to the leaderboard)')
                    if name == None:
                        break
                    elif name == "":
                        print('error')
                        messagebox.showerror("Error", "Name can not be empty!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif name.isspace() == True:
                        messagebox.showerror("Error", "Name can not be spaces only!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif len(name) > 10:
                        messagebox.showerror("Error", "Name can not be longer than 10 characters!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    else:
                        showinfo('Highscore', 'Hi {}, congrats with your score!\nYour score is added to the leaderboard!'.format(name))
                        edit_leaderboard(30, s30p3, name)
                        break


        elif time_countdown == 60:
            if score > s60p3:
                while True:
                    name = askstring('Highscore!', 'You hit a new highscore!\nWe would like to know your name for the leaderboard!\n(if you press cancel you will not be added to the leaderboard)')
                    if name == None:
                        break
                    elif name == "":
                        print('error')
                        messagebox.showerror("Error", "Name can not be empty!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif name.isspace() == True:
                        messagebox.showerror("Error", "Name can not be spaces only!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    elif len(name) > 10:
                        messagebox.showerror("Error", "Name can not be longer than 10 characters!\n\npress 'cancel' if you don't want to be added to the leaderboard")
                        
                    else:
                        showinfo('Highscore', 'Hi {}, congrats with your score!\nYour score is added to the leaderboard!'.format(name))
                        edit_leaderboard(60, s60p3, name)
                        break
                            
                


def edit_leaderboard(seconds, score_beaten, name):
    global connection, score
    sql_select_Query = "select * from highscores_game"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    for row in records:
        if row[1] == seconds:
            if row[3] == score_beaten:
                number = row[0]
                sql_update_query = """Update highscores_game set name = %s, score = %s where id = %s"""
                input = (name, score, number)
                cursor.execute(sql_update_query, input)
                connection.commit()
                break

                
def choose_location():
    global xcoord, ycoord, score, score_label, kill, time_countdown
    if kill == True:
        after_game()
    else:
        score +=1
        score_label.configure(text="SCORE: {}".format(str(score)))
        #xcoord = random.randint(13, 1445)
        #ycoord = random.randint(70, 770)
        ycoord = random.randint(70, (root.winfo_height() - 110))
        xcoord = random.randint(13, (root.winfo_width() - 130))
        make_button()



def timer():
    global t1, t2, root, kill, timer_label, time_countdown
    time = time_countdown
    for i in range(time, -1, -1):
        timer_label.configure(text="TIME: {}".format(str(i)))
        sleep(0.8)
    kill = True

    
def make_button():
    global cframe, xcoord, ycoord, button
    try:
        button.destroy()
    except NameError:
        pass
    button.destroy()
    button = HoverButton(root, activebackground='#c7c7c7', text="", fg="black", bg="green", font=('Helvetica', '20'), width=4, height=1, command=lambda: choose_location())
    button.pack()
    button.place(x=xcoord,y=ycoord)


def click():
    global label, score, score_label, t1, t2, timer_label
    score = 0
    score_label.grid(row=0, column=0, padx=(0, 0), pady=(15, 0))
    timer_label.grid(row=0, column=1, padx=(10, 0), pady=(15, 0))
    label.destroy()

    t1 = Thread(target=timer)
    t1.setDaemon(True)
    t1.start()
    t2 = Thread(target=choose_location)
    t2.setDaemon(True)
    t2.start()



#######################################3
def delete_screen():
    s = root.winfo_children()

    for i in s:
        try:
            i.destroy()
        except:
            i.delete()
    root.config(bg="SystemButtonFace")


class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground

def connect_mysql():
    global connected, connection
    try:
        connection = mysql.connector.connect(host='',
                                         database='',
                                         user='',
                                         password='')
        connected = True
        home_page()
    
    except mysql.connector.Error as error:
        connected = False
        messagebox.showerror("Database Error", "Can not connect to online database!\n\nYou can still play the game however the highscores will not be shown or edited")
        home_page()

def loading():
    l = tk.Label(root, text="Please wait!\nIt takes some time to connect to the database!", font=('Helvetica', '50'))
    l.pack(pady=150)
    connect_mysql()

connected = False
loading()
root.mainloop()

import os
from tkinter import *
from turtle import *
from datetime import datetime
import time

print("""
#####  #####  ####     #####  #####  #####  #####  #####  #####  #####  #   #  #####
#      #      #   #    #   #  #      #        #    #        #    #   #  ##  #    #  
#####  #####  ####     #####  #####  #####    #    #####    #    #####  # # #    #  
    #  #      #   #    #   #      #      #    #        #    #    #   #  #  ##    #  
#####  #####  ####     #   #  #####  #####  #####  #####    #    #   #  #   #    #  
""")
print("Welcome, ", os.getlogin(),"!")
running = True
while running:
    do = input("//")
    if do == 'help':
        print("""
        List of commands:
        help - displays this help list
        yinyang - draws yin yang
        terminal - allows you to use your system terminal, will ask you what command to run
        hello - spams Hello World!
        clock - opens a graphical clock
        exit - closes Seb Assistant
        """)
    if do == 'yinyang':
        print("The code used to generate the yinyang drawing belongs to the Python.org")
        TurtleScreen._RUNNING = True
        def yin(radius, color1, color2):
            width(3)
            color("black", color1)
            begin_fill()
            circle(radius/2., 180)
            circle(radius, 180)
            left(180)
            circle(-radius/2., 180)
            end_fill()
            left(90)
            up()
            forward(radius*0.35)
            right(90)
            down()
            color(color1, color2)
            begin_fill()
            circle(radius*0.15)
            end_fill()
            left(90)
            up()
            backward(radius*0.35)
            down()
            left(90)

        def yang():
            reset()
            yin(200, "black", "white")
            yin(200, "white", "black")
            ht()
        yang()
        mainloop()
    if do == 'terminal':
        terminalcmd = input("Command: ")
        os.system(terminalcmd)
    if do == 'hello':
        print("Are you sure? (lowercase only)")
        helloworldyn = input("[y] ")
        if helloworldyn == 'y':
            while 1 < 2:
                print("Hello World!")
    if do == 'clock':
        print("The code used to generate the graphical clock belongs to the Python.org")
        TurtleScreen._RUNNING = True
        def jump(distanz, winkel=0):
            penup()
            right(winkel)
            forward(distanz)
            left(winkel)
            pendown()

        def hand(laenge, spitze):
            fd(laenge*1.15)
            rt(90)
            fd(spitze/2.0)
            lt(120)
            fd(spitze)
            lt(120)
            fd(spitze)
            lt(120)
            fd(spitze/2.0)

        def make_hand_shape(name, laenge, spitze):
            reset()
            jump(-laenge*0.15)
            begin_poly()
            hand(laenge, spitze)
            end_poly()
            hand_form = get_poly()
            register_shape(name, hand_form)

        def clockface(radius):
            reset()
            pensize(7)
            for i in range(60):
                jump(radius)
                if i % 5 == 0:
                    fd(25)
                    jump(-radius-25)
                else:
                    dot(3)
                    jump(-radius)
                rt(6)

        def setup():
            global second_hand, minute_hand, hour_hand, writer
            mode("logo")
            make_hand_shape("second_hand", 125, 25)
            make_hand_shape("minute_hand",  130, 25)
            make_hand_shape("hour_hand", 90, 25)
            clockface(160)
            second_hand = Turtle()
            second_hand.shape("second_hand")
            second_hand.color("gray20", "gray80")
            minute_hand = Turtle()
            minute_hand.shape("minute_hand")
            minute_hand.color("blue1", "red1")
            hour_hand = Turtle()
            hour_hand.shape("hour_hand")
            hour_hand.color("blue3", "red3")
            for hand in second_hand, minute_hand, hour_hand:
                hand.resizemode("user")
                hand.shapesize(1, 1, 3)
                hand.speed(0)
            ht()
            writer = Turtle()
            writer.ht()
            writer.pu()
            writer.bk(85)

        def wochentag(t):
            wochentag = ["Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday", "Sunday"]
            return wochentag[t.weekday()]

        def datum(z):
            monat = ["Jan.", "Feb.", "Mar.", "Apr.", "May", "June",
                     "July", "Aug.", "Sep.", "Oct.", "Nov.", "Dec."]
            j = z.year
            m = monat[z.month - 1]
            t = z.day
            return "%s %d %d" % (m, t, j)

        def tick():
            t = datetime.today()
            sekunde = t.second + t.microsecond*0.000001
            minute = t.minute + sekunde/60.0
            stunde = t.hour + minute/60.0
            try:
                tracer(False)
                writer.clear()
                writer.home()
                writer.forward(65)
                writer.write(wochentag(t),
                             align="center", font=("Courier", 14, "bold"))
                writer.back(150)
                writer.write(datum(t),
                             align="center", font=("Courier", 14, "bold"))
                writer.forward(85)
                tracer(True)
                second_hand.setheading(6*sekunde)
                minute_hand.setheading(6*minute)
                hour_hand.setheading(30*stunde)
                tracer(True)
                ontimer(tick, 100)
            except Terminator:
                pass

        def main():
            tracer(False)
            setup()
            tracer(True)
            tick()
        mode("logo")
        msg = main()
        mainloop()
    if do == "exit":
        print("""
####   #   #  #####  ####
#   #  #   #  #      ###
####   #####  #####  ##
#   #    #    #       
####     #    #####  #
        """)
        print("Goodbye!")
        time.sleep(2.5)
        running = False
        

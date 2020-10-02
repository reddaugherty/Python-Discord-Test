import time
import pyautogui
import random
#pyautogui failsafe. move cursor to top left of screen to cancel script
pyautogui.FAILSAFE = True

#making a list of messages to send
list = ["ez rank up", "im not cheating, im just using my resources", "this took me waayy too long to figure out"]

#wait for 2 seconds
##time.sleep(2)


while True:
    #click in discord text box
    pyautogui.click(x=561, y=1325)
    #type a random message from a list
    pyautogui.write(random.choice(list))
    #press enter to send message
    pyautogui.press('enter')
    #wait for half a second
    time.sleep(.5)
    #get rank
    pyautogui.write("!rank")
    pyautogui.press('enter')
    #pause for 1 minute
    time.sleep(60)

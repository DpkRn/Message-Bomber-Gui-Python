import pyautogui as rb
import time 
rb.alert("Goto To At Your Location You have 5 sec:",title="Message Bomber: Created By Deepak")
time.sleep(5)
while(rb.confirm('Have You Placed Your Cursor At Your Place:',title="Deepak Asking", buttons=['Ok','Not Yet'])=='Not Yet'):
    time.sleep(5)
msg=rb.prompt("Enter Your Message:",title="To Cancel,Press cancel button Anytime",default='')
if msg!='' and msg!=None:  
    no=rb.prompt("Enter Number of times you Want to Send:",title="To Cancel,Press cancel button Anytime",default='')
    if no!='' and type(no)!=int and no!=None:
        for i in range(0,int(no)):
            rb.write(msg)
            rb.press("enter")
            time.sleep(1)
    else:
        rb.alert("Required Integer in Seconds ex: 5",title="Warning ! Start Apps again:")
else:
    rb.alert("InputBox Cann't be blank",title="Warning ! Start Apps again:")



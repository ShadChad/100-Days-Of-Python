import os
import time

# from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox

# def display_notification():
#     app = QApplication([])
#     window = QWidget()
#     QMessageBox.information(window,"Notification Remainder","Plese take a break and go drink a glass of water")
#     window.show()
#     app.exec_()


# while True:
#     display_notification()
#     time.sleep(5)

# using os module, couldnt recognize toast.exe

# def send_notification(title,message):
#     command = f'toast.exe /t:"{title}" "{message}"'

#     os.system(command)

# while True:
#     send_notification("Notification","Drink water")
#     time.sleep(5)


#using notify

from winotify import Notification,audio

toast = Notification(app_id="Shady Script",
                     title = "Water Remainder",
                     msg= "Drink Water Remainder",
                     duration="long",
                     icon="C:\\Users\\subed\\Pictures")


toast.set_audio(audio.Default,loop = False)
while True:
    toast.show()
    time.sleep(30*60)


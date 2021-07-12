#This Program is a Desktop notifier that notifies the user to drink water after every one hour
import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title = '******Reminder******',
            message = 'This is a reminder to drink water. \nStay Hydrated :)',
            app_icon = 'C:\Users\Aishani Anavkar\PycharmProjects\pythonProject\glass_of_water_icon.ico',
            timeout = 5
        )
        time.sleep(3600)
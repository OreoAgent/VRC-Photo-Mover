import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import shutil

#VERY important variables
Vrchat_photo_folder = "temp" #change this to the location of which vrchat originally saves the folder

new_folder = "temp" #change this to the location of the next folder you WANT the images to be saved to.

#classes because why the bloody hell not
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'File created: {event.src_path}')
        time.sleep(0.5)
        shutil.move(event.src_path, new_folder)
        print(f"Moved {event.src_path} to {new_folder}")


#the main loop

#initialising rubbish
event_handeler = MyHandler()
observer = Observer()
observer.schedule(event_handeler, path = Vrchat_photo_folder, recursive = True)

#the observer (that sounds spooky, i like it. Sounds like a horror movie.)

observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()


"""
Hey! Thank you so much for downloading this! I made this because F****** VRCHAT WONT F****** ADD A WAY TO CHANGE WHERE YOU F****** PHOTOS GET F****** SAVED!

Sorry about that, but I made this because vrchat wont allow you to easily change the location where your photos get saved.

This should make it so that when your vrchat photos get taken, it will move it to the location of your choice.
"""

"""
So, need some help with the actual program working? Documentation will be coming soon, but for now, here are a few pointers.

1) Path

Make it so that when the path is entered into the variable, on line 7 and 9, it has double back slashes (for example: c:\\user\\photos\\vrchat)


2) Observer

If it isnt working for you, make sure you have watchdog installed. You can do this by typing the following in the terminal: pip install watchdog
"""
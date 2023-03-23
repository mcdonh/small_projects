"""
Using watchdog to trigger from system events automatically sorts downloads folder
"""
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler




class MyHandler(FileSystemEventHandler):
    """Class for file system"""
    def on_modified(self,event):
        for filename in os.listdir(FOLDER_TO_TRACK):
            src = FOLDER_TO_TRACK + "/" + filename
            new_destination = FOLDER_DESTINATION + "/" + filename
            os.rename(src, new_destination)


FOLDER_TO_TRACK = "/Users/---/Downloads"
FOLDER_DESTINATION = "/Users/---/"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, FOLDER_TO_TRACK, recursive=True)
observer.start()


try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

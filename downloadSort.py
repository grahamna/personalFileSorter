import os
from shutil import move
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

sourceDir = "C:\\Users\\natea\\Downloads\\keep"
destMusic = "C:\\Users\\natea\\Music"
destImg = "C:\\Users\\natea\\OneDrive\\Pictures\\temp"
destPDF = "C:\\Users\\natea\\OneDrive\\Textbooks\\temp"

# a static method to move files to their respective folders based on their file extension type 
class moverHandler():
    def __init__(self, src_path):
        fileName = src_path
        dest = sourceDir
        if  fileName.endswith(".png") or fileName.endswith(".jpg") or fileName.endswith(".jpeg"):
            dest = destImg
            move(fileName, dest)
            print(fileName +" move to " + dest +" from " + sourceDir)
        elif fileName.endswith(".mp3") or fileName.endswith(".wav"):
            dest = destMusic
            move(fileName, dest)
            print(fileName +" move to " + dest +" from " + sourceDir)
        elif fileName.endswith(".pdf"):
            dest = destPDF
            move(fileName, dest)
            print(fileName +" move to " + dest +" from " + sourceDir)
        else:
            print("File type of "+ fileName+ " not recognized. Did nothing.")
            
class OnMyWatch:
    watchDirectory = sourceDir
    def __init__(self):
        self.observer = Observer()
    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.watchDirectory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
        self.observer.join()
  
  
class Handler(LoggingEventHandler):
    @staticmethod
    def on_any_event(event):
        if event.is_directory or event.src_path == sourceDir+"\\script.sh" or event.src_path == sourceDir+"\\downloadSort.py":
            return None
        elif event.event_type == 'created':
            print("Watchdog received created event - % s." % event.src_path)
            moverHandler(event.src_path)
        elif event.event_type == 'modified':
            print("Watchdog received modified event - % s." % event.src_path)
            
              
  
if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()

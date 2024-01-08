import time
import os
import argparse
import subprocess
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

class MediaWatcher:
    def __init__(self, directory):
        self.directory = directory
        self.observer = Observer()
        self.spawnedProcess = None
        ls = os.listdir(directory)
        fileToPlay = [f for f in ls if f.startswith("toplay.")]
        if fileToPlay:
            self.playFile(directory + "/" + fileToPlay[0])

 
    def run(self):
        event_handler = PatternMatchingEventHandler(
            patterns=["toplay.*"],
            ignore_patterns=[],
            ignore_directories=True)
        event_handler.on_any_event = self.onEvent
        self.observer.schedule(event_handler, self.directory, recursive = True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")
 
        self.observer.join()
    
    def onEvent(self, event):
        if event.event_type == 'modified':
            self.playFile(event.src_path)
        elif event.event_type == 'deleted':
            self.stopPlayback()
    
    def stopPlayback(self):
        if self.spawnedProcess:
            self.spawnedProcess.kill()

    def playFile(self, file):
        if self.spawnedProcess:
            self.spawnedProcess.kill()
        self.spawnedProcess = subprocess.Popen(['cvlc', '--no-video-title-show', '-f', '--loop', file])

 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "Media scanner")
    parser.add_argument('-d', '--directory', required=True)
    args = parser.parse_args()

    watch = MediaWatcher(os.path.join(args.directory))
    watch.run()
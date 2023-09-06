import os
import time
from build import process_file
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# A python script that uses the watchdog package to watch for changes in the src folder
# and rebuild the build folder when changes are detected.

def start_watcher():
    class Handler(FileSystemEventHandler):
        def on_modified(self, event):
            print(f'File {event.src_path} has been modified')
            process_file(event.src_path, False)

    observer = Observer()
    observer.schedule(Handler(), path=os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')), recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == '__main__':
    start_watcher()
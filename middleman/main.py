import watchdog.events
import watchdog.observers
import json
from core.archive import Archive
from core.worker import worker
import time
import enum
import os



class Handler(watchdog.events.PatternMatchingEventHandler):
    worker = worker()

    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*md.json'],
                                                             ignore_directories=True, case_sensitive=False)

    def on_created(self, event):
        print("Watchdog received created event - % s." % event.src_path)

    # collection.append({'collection': i['collection'], 'title': i['title'], 'mediatype': i['mediatype']})
    # Event is created, you can process it now

    def on_modified(self, event):
        print('File name :    ', os.path.basename(__file__))

        worker.clear_list(self)
        print("Watchdog received modified event - % s." % event.src_path)
        f = open('data/md.json')
        data = json.load(f)
        for i in data['documents']:
            worker.process_list(event, i['collection'], i['title'], i['mediatype'], i['file'])
            # worker.popCollection0th(self)

            time.sleep(.15)
        Archive.fulfillment(self)


if __name__ == "__main__":
    src_path = r"."
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

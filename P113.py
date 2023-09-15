def on_created(self, event):
    print("Hey, {event.src_path} has been created!")

def on_deleted(self, event):
    print("Oops! Someone deleted {event.src_path}!")

def on_modified(self, event):
    print("Hey there!, {event.src_path} has been modified")

def on_moved(self, event):
    print("Someone has moved {event.src_path} to {event.dest_path}")

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("Stopped!")
    observer.stop
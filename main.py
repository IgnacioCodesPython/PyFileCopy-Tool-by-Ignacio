from pycopier import shutil
from os import system


def start():
    filepath = input("What's the file's path that you would like to move?\n")
    filename = input("What's the filename of the file that you would like to move?\n")
    filenewpath = input("What's the path that you would like to move your file?\n")
    complete = input( f"You've entered the current parameters:\nFile path: {filepath}\nFile name: {filename}\nCopy path: {filenewpath}\nIs that the settings you wanted?\n")
    if complete == "Yes":
        print("Great! First let's open the directories.")
        system(f"explorer {filepath}")
        system(f"explorer {filenewpath}")
        print("With the directories open, you'll see how the file is moved instantly.")
        print("Okay, so with that out of the way, let's start.")
        try:
            shutil.move(f"{filepath}/{filename}", filenewpath)
        except FileNotFoundError:
            print("Oh no... The file was not found: 1. Please restart the program and try again with other file that exists on your hard drive, or thumb drive, or any single device that you have. Bye.")
            exit(1)
        print("Done! Did you see it? Good. Let's finish over here with all of that Python magic, and goodbye.")
    else:
        print("Okay, how about this?")
        start()


start()

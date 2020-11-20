# This script provides an interface for end users accessing this repository through repl.it to run
# individual challenges. If you're looking at this repo on GitHub or your local machine, this file probably isn't
# of any relevance to you.

import os
import random
import re

rand_dir = random.choice([f.name for f in os.scandir() if f.is_dir() and f.name not in [".idea", ".git"]])
rand_script = random.choice([f for f in os.listdir(rand_dir) if f.endswith(".py")])
example_path = f"{rand_dir}/{rand_script}"

path = input(f"\nType the file path of the Python script you wish to run (e.g. {example_path}).\n"
             "Not all scripts print output to the console and/or are accompanied by unit tests (yet), so you might\n"
             "have to play around with things a bit (read: add print statements and/or unit tests yourself) "
             "in order to\n"
             "actually see what the code produces.\n"
             "\n"
             "File paths are not case sensisitve.\n"
             "\n"
             "For more granular control over file execution, clone this repl's GitHub repository to your local "
             "machine.\n"
             "https://github.com/jasonalantolbert/coding-challenges\n"
             ""
             "\n"
             "> ")

while True:
    try:
        directory, script = re.split(r"[/\\]", path)
    except ValueError:
        print(
            "It seems you entered an incorrectly-formatted file path. Make sure you're including both the directory\n"
            f"name and file name, separated by a single forward or backward slash (e.g. {example_path}).")
        path = input("> ")
        continue

    try:
        os.chdir(directory)
    except FileNotFoundError:
        os.chdir("..")
        print("It seems that directory doesn't exist. Check your spelling, perhaps?")
        path = input("> ")
        continue

    try:
        exec(open(script).read())
    except FileNotFoundError:
        print("It seems that file doesn't exist. Check your spelling, " + ("perhaps?" if script.endswith("py") else
                                                                           "and don't forget the .py extension."))
        os.chdir("..")
        path = input("> ")
        continue

    os.chdir("..")
    print("\nEND FILE EXECUTION\n")
    path = input("If you'd like to run another file, enter it's path:\n> ")

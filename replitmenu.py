# This script provides an interface for end users accessing this repository on Repl.it to run
# individual challenges. If you're looking at this repo on GitHub or your local machine, this file probably isn't
# of any relevance to you.

import os
import random
import re

import colorama
from unipath import Path

colorama.init(autoreset=True)


def get_example_path():
    while True:
        try:
            rand_dir = random.choice([
                f.name for f in os.scandir()
                if f.is_dir() and f.name not in [".idea", ".git"]
            ])
            rand_script = random.choice(
                [f for f in os.listdir(rand_dir) if f.endswith(".py")])
        except IndexError:
            continue

        return f"{rand_dir}/{rand_script}"


path = input(
    f"\nType the file path of the Python script you wish to run (e.g. {get_example_path()}).\n"
    "Not all scripts print output to the console and/or are accompanied by unit tests (yet), so you might\n"
    "have to play around with things a bit (read: add print statements and/or unit tests yourself) "
    "in order to\n"
    "actually see what the code produces.\n"
    "\n"
    "Currently, unit tests will terminate the program after they run.\n"
    "\n"
    "On Repl.it, file paths are case sensitive.\n"
    "\n"
    "For more granular control over file execution, clone this repl's GitHub repository to your local "
    "machine.\n"
    "https://github.com/jasonalantolbert/coding-challenges\n"
    "\n"
    "> ")

while True:
    try:
        directory, script = re.split(r"[/\\]", path)
    except ValueError:
        if "replitmenu.py" in path:
            path = input("Very funny. Enter the file path to a challenge script, please.\n> ")
            continue
        else:
            print(
                "It seems you entered an incorrectly formatted file path. Make sure you're including both the "
                "directory\n"
                f"name and file name, separated by a single forward or backward slash (e.g. {get_example_path()})."
            )
            path = input("> ")
            continue

    try:
        os.chdir(directory)
    except FileNotFoundError or OSError:
        print(
            "It seems that directory doesn't exist. Check your spelling, perhaps?\n"
            "Remember, on Repl.it, file paths "
            "are case sensitive.")
        path = input("> ")
        continue

    try:
        file = open(script).read()
    except FileNotFoundError:
        print("It seems that file doesn't exist. Check your spelling, " +
              ("perhaps? " if script.
               endswith(".py") else "and don't forget the .py extension.") +
              "\nRemember, on Repl.it, file paths are case sensitive.")
        os.chdir(Path(os.getcwd()).parent)
        path = input("> ")
        continue
    else:
        if script == "tests.py":
            print(
                colorama.Fore.LIGHTRED_EX + "The program will terminate after this file finishes execution. "
                                            "Continue anyway? [yes/no]")
            choice = input("> ")
            if choice in ["no", "n"]:
                os.chdir(Path(os.getcwd()).parent)
                path = input("Enter a file path:\n> ")
                continue
            else:
                print(colorama.Fore.GREEN + f"\nBEGIN FILE EXECUTION ({directory}/{script})\n")
        else:
            print(colorama.Fore.GREEN + f"\nBEGIN FILE EXECUTION ({script})\n")

        exec(file)

    os.chdir(Path(os.getcwd()).parent)
    print(colorama.Fore.LIGHTRED_EX + f"\nEND FILE EXECUTION ({script})\n")
    previous = path
    path = input("If you'd like to run another file, enter its path (or leave blank to run the "
                 "previous file again):\n> ")
    if not path:
        path = previous

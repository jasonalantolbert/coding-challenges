import random
import os
import re

directory = random.choice([f.name for f in os.scandir() if f.is_dir() and f.name not in [".idea", ".git"]])
script = random.choice([f for f in os.listdir(directory) if f.endswith(".py")])

path = input(f"\nType the file path of the Python script you wish to run (e.g. {directory}/{script}).\n"
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

exec(open(path).read())

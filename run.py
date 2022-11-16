import os
from pathlib import Path
from rich import print
from rich.prompt import Prompt
from multithreading_demo import multithreading_demo
from demo import demo

choice = input("\nWelcome to the Virginia DMV Plate Availability Checker!\n\nWould you like to check input a plate to check or read from file? \n\n1. Input plate names.\n2. Read from a text file provided in the \"words\" directory.\n\n")
data_folder = Path('words')
while True:
    if choice == "1":
        demo()
        break
    elif choice == "2":
        print("",os.listdir(data_folder))
        file = input(f"\nPlease enter the file name without .txt\n")
        multithreading_demo(file + ".txt")
        break
    else:
        choice = Prompt.ask(f"[red]Invalid input. Please try again[/red]")
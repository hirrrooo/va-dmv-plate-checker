import multiprocessing.dummy as mp
import os
from pathlib import Path
from rich import print
from PlateAPI import API

def multithreading_demo(file):
  obj = API()
  data_folder = Path('words')
  words = open(data_folder/file).read().splitlines() 
  # words = open("words.txt", "r").read().splitlines()
  print(f"[green]Loaded {len(words)} words\n")
  with open("./output.txt", "w") as output:
    word_list = [word.strip() for word in words]  #if word.strip().isalpha() and len(word.strip()) == 2]
    availability_count = 0
    def check(word):
      print(f"Query:[#FFA500] {word.upper()}")
      query = obj.check_plate(plate=word)
      if query == True:
        print(f"[green]Available: {query}\n")
        availability_count =+ 1
      if query:
        output.write(f"{word.upper()}\n")
      else:
        print(f"[red]Available: {query}\n")
    p = mp.Pool(1)
    p.map(check, word_list)
    p.close()
    p.join()
  print(f'{availability_count} plates [bold green]available[/bold green] out of {len(words)}\nView available plates in [bold]output.txt[bold]')
  if __name__ != '__main__': # If ran directly, don't ask to run again.
    run_again = input("Would you like to run another file? (y/n): ")
    if run_again == "y":
      data_folder = Path('words')
      print("",os.listdir(data_folder))
      file = input(f"\nPlease enter the file name without .txt\n")
      multithreading_demo(file + ".txt")
    elif run_again == "n":
      quit()
    else:
      print(f"[red]Invalid input.[/red]")

if __name__ == '__main__':
  multithreading_demo('example.txt') # If running this file directly, change this to the file you want to check.
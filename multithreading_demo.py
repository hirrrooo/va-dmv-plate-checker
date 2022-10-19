from PlateAPI import API
from colorama import Fore, Style
import multiprocessing.dummy as mp


obj = API()
words = open("ccc.txt", "r").read().splitlines() 
# words = open("words.txt", "r").read().splitlines()

with open("./output.txt", "w") as output:
  word_list = [word.strip() for word in words]  #if word.strip().isalpha() and len(word.strip()) == 2]
  def check(word):
    print(f"Query: {word.upper()}")
    query = obj.check_plate(plate=word)
    if query == True:
      print(f"{Fore.GREEN}Available: {query}{Style.RESET_ALL}\n")
    else:
      print(f"{Fore.RED}Available: {query}{Style.RESET_ALL}\n")
    if query:
      output.write(f"{word.upper()}\n")

  p = mp.Pool(1)
  p.map(check, word_list)
  p.close()
  p.join()
from PlateAPI import API
import multiprocessing.dummy as mp
import colorama

obj = API()
words = open("every2lettercombo.txt", "r").read().splitlines() 
# words = open("words.txt", "r").read().splitlines()

with open("./output.txt", "w") as output:
  word_list = [word.strip() for word in words]  #if word.strip().isalpha() and len(word.strip()) == 2]
  def check(word):
    print(f"Query: {word.upper()}")
    query = obj.check_plate(plate=word)
    print(f"Available: {query}\n")
    if query:
      output.write(f"{word.upper()}\n")
  p = mp.Pool(1)
  p.map(check, word_list)
  p.close()
  p.join()
from PlateAPI import API
from colorama import Fore, Style
obj = API()

while True:
  plate_number = input("Plate Number: ")
  print(f"\n{Fore.WHITE}Query Plate: {plate_number}{Style.RESET_ALL}")
  query = obj.check_plate(plate=plate_number)
  if query == True:
      print(f"{Fore.GREEN}Available: {query}{Style.RESET_ALL}\n")
  else:
      print(f"{Fore.RED}Available: {query}{Style.RESET_ALL}\n")
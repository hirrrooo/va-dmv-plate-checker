from PlateAPI import API
from colorama import Fore, Style
obj = API()

while True:
  plate_number = input("Plate Number: ")
  print(f"Query Plate: {plate_number}")
  query = obj.check_plate(plate=plate_number)
  print(f"Available: {query}{Style.RESET_ALL}")
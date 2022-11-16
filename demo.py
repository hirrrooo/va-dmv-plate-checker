from rich import print
from PlateAPI import API

def demo():
    obj = API()
    while True:
        plate_number = input("\nPlate Number: ")
        print(f"Query Plate:[#FFA500] {plate_number}")
        query = obj.check_plate(plate = plate_number)
        if query == None:
            demo()
        elif query == True:
            print(f"[green]Available: {query}\n")
        else:
            print(f"[red]Available: {query}\n")

if __name__ == '__main__':
    demo()
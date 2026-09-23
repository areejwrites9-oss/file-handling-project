from os import path
from pathlib import Path


def readfileandfolder():
  path = Path('.')
  items = list(path.rglob('*'))
  for i, item in enumerate(items, start=1):
        print(f"{i}: {item}")


def createfile():
    try:
        readfileandfolder()
        name = input("Enter the name of file: ").strip()
        if not name:
            print("File name cannot be empty.")
            return

        p = Path(name)
        if not p.exists():
            with open(p, "w", encoding="utf-8") as fs:
                data = input("Enter the data you want to write: ")
                fs.write(data)
            print("YOUR FILE IS CREATED")
        else:
            print("This file already exists in your computer.")
    except Exception as err:
        print(f"An error occurred as {err}")


def readfile():
    try:
        readfileandfolder()
        name = input("Enter the name of your file: ").strip()
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p, "r", encoding="utf-8") as fs:
                print(fs.read())
        else:
            print("This file does not exist.")
    except Exception as err:
        print(f"An error occurred as {err}")


def upgradefile():
    try:
        readfileandfolder()
        name = input("Enter name of your file: ").strip()
        p = Path(name)
        if not p.exists() or not p.is_file():
            print("This file does not exist.")
            return

        print("Press 1 to append data to file")
        print("Press 2 to overwrite data to file")
        print("Press 3 to change the name")
        response = int(input("Enter your response: "))

        if response == 1:
            with open(p, "a", encoding="utf-8") as fs:
                data = input("What do you want to write? ")
                fs.write(data)
            print("Data appended.")
        elif response == 2:
            with open(p, "w", encoding="utf-8") as fs:
                data = input("What do you want to write? ")
                fs.write(data)
            print("File overwritten.")
        elif response == 3:
            new_name = input("Enter the new file name: ").strip()
            if not new_name:
                print("New file name cannot be empty.")
                return
            p.rename(new_name)
            print("File renamed.")
        else:
            print("Invalid option selected.")
    except ValueError:
        print("Please enter a valid number.")
    except Exception as err:
        print(f"An error occurred as {err}")


def deletefile():
    try:
        readfileandfolder()
        name = input("Enter the name of your file: ").strip()
        p = Path(name)
        if p.exists() and p.is_file():
            p.unlink()
            print("Your file is deleted.")
        else:
            print("This file does not exist.")
    except Exception as err:
        print(f"An error occurred as {err}")


def main():
    while True:
        print("1 - CREATE FILE")
        print("2 - READ FILE")
        print("3 - UPDATE FILE")
        print("4 - DELETE FILE")
        print("5 - EXIT")

        choice = input("Enter your response: ").strip()

        if choice == "1":
            createfile()
        elif choice == "2":
            readfile()
        elif choice == "3":
            upgradefile()
        elif choice == "4":
            deletefile()
        elif choice in ("5", "exit", "Exit"):
            print("Goodbye!")
            break
        else:
            print("Sorry, you have entered a wrong number.")


if __name__ == "__main__":
    main()


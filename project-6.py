from datetime import datetime

class Journal:

    def __init__(self):
        self.filename = "journal.txt"

    def add_entry(self):
        entry = input("Enter Your Entry: ")

        file = open(self.filename, "a")
        file.write("Date : " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
        file.write("Note : " + entry + "\n\n")
        file.close()

        print("Entry Saved Successfully")

    def view_entry(self):
        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if content:
                print("\nJournal Entries\n")
                print(content)
            else:
                print("Journal Is Empty")

        except:
            print("Journal File Not Found")

    def search_entry(self):
        word = input("Enter Word To Search: ")

        try:
            file = open(self.filename, "r")
            content = file.read()
            file.close()

            if word.lower() in content.lower():
                print("\nEntry Found\n")
                print(content)
            else:
                print("No Matching Entry")

        except:
            print("Journal File Not Found")

    def delete_entry(self):
        answer = input("Delete All Entries (yes/no): ")

        if answer.lower() == "yes":
            file = open(self.filename, "w")
            file.close()
            print("All Entries Deleted")
        else:
            print("Delete Cancelled")


journal = Journal()

while True:

    print("\nPersonal Journal")
    print("1. Add Entry")
    print("2. View Entries")
    print("3. Search Entry")
    print("4. Delete Entries")
    print("5. Exit")

    choice = input("User Input: ")

    if choice == "1":
        journal.add_entry()

    elif choice == "2":
        journal.view_entry()

    elif choice == "3":
        journal.search_entry()

    elif choice == "4":
        journal.delete_entry()

    elif choice == "5":
        print("Thank You")
        break

    else:
        print("Invalid Choice")
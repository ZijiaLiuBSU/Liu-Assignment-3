students = {}

with open("students.txt", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        if len(parts) == 5:
            sid, last, first, major, gpa = parts
            students[sid] = [last, first, major, gpa]

def show_menu():
    print("\nChoose an option:")
    print("1) Search by Last Name")
    print("2) Search by Major")
    print("3) Quit")

def search_last_name(name):
    found = False
    for sid, info in students.items():
        if info[0].lower() == name.lower():
            print(f"{sid}, {info[0]}, {info[1]}, {info[2]}, {info[3]}")
            found = True
    if not found:
        print("We cannot find this last name.")

def search_major(major):
    found = False
    for sid, info in students.items():
        if info[2].lower() == major.lower():
            print(f"{sid}, {info[0]}, {info[1]}, {info[2]}, {info[3]}")
            found = True
    if not found:
        print("We cannot find this major.")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter last name to search for: ")
        search_last_name(name)
    elif choice == "2":
        major = input("Enter major to search for: ")
        search_major(major)
    elif choice == "3":
        print("Thank you for using the system, Bye.")
        break
    else:
        print("Invalid option, please try again")

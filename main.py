import datetime
import csv

#csv filename
filename = "expenses_save.csv"

#This will generate the day's date
date = datetime.date
today = date.today() #Returns today's date as yyyy/mm/dd

def save_file(expense_list):
    print("Saving your records...")
    if not expense_list:
        print("You have no records to save. See you later")
        exit()
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        fieldnames = expense_list[0].keys()
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expense_list)

    print("Your expenses have been saved to ", filename)

def load_file():
    list_of_expenses = []
    print("Loading save file...")
    try:
        with open(filename, mode="r") as file:
            reader = csv.DictReader(file)
            #This ensures that the list is clear before appending
            list_of_expenses.clear()

            for row in reader:
                #This ensures that id is loaded as a type 'int'
                row["id"] = int(row["id"])
                #This ensure that amount is loaded as type 'float'
                row["amount"] = float(row["amount"])
                list_of_expenses.append(row)
            print("The program has successfully loaded your record")
    except FileNotFoundError:
        print("There was no save file to load from. Starting with a scrubbed record")

    return list_of_expenses


def add(expense_list, exp_id):
    amount = float(input("Enter the amount of your expense: "))
    description = input("What did you spend this money on: ")
    exp_id += 1

    expense = {"id":exp_id, "date":today.strftime("%Y-%m-%d"), "description":description, "amount":amount}
    expense_list.append(expense)
    print("You've added a new expense")

    return expense_list, exp_id

def delete(expense_list):
    delete_id = int(input("Enter the id of the expense you want to delete: "))

    #This will create a new list without the deleted entry
    new_list = [item for item in expense_list if item["id"] != delete_id]

    if len(new_list) == len(expense_list):
        print(f"No expense found with id {delete_id}.")
    else:
        print(f"The expense with id number {delete_id} has been removed.")
    return new_list

def update(expense_list):
    exp_id = int(input("Enter the id number for the expense you want to update: "))
    for item in expense_list:
        if item["id"] == exp_id:
            print(f"{item["id"]}  {item["date"]}     {item["description"]}      {item["amount"]}")
            print("What do you want to update in this expense?")
            print("1. Description\n2. Amount")
            choice = int(input("Make your choice: "))
            try:
                if choice == 1:
                    new_desc = input("Enter a new description: ")
                    item["description"] = new_desc
                    print(f"The description for Expense with id {exp_id} has been updated.")
                elif choice == 2:
                    new_amount = int(input("Enter a new amount: "))
                    item["amount"] = new_amount
                    print(f"The amount for Expense with id {exp_id} has been updated.")
                else:
                    print("You have entered a wrong option")
                    program_interface()
            except ValueError:
                print("You're trying to edit a non-existent property")
                break
    return expense_list

def expense_summary(expense_list):
    total = sum(item["amount"] for item in expense_list)
    print(f"Total Expenses: ${total}")

def print_expenses(expense_list):

    if not expense_list:
        print("You currently have no recorded expenses")
    print("Here are your expenses so far")
    print(f'{"ID":<3} {"Date":<12} {"Description":<20} {"Amount":<8}')

    for item in expense_list:
        print(f'{item["id"]:<3} {item["date"]:<12} {item["description"]:<20} ${item["amount"]:<8}')
    print("Done")

def program_interface():
    global start_file
    start_file = load_file()
    expense_id = max((expense["id"] for expense in start_file), default=0)

    while True:
        print("="*100)
        print("Welcome to your Expense Tracker")
        print("What would you like to do?")
        print("1. Add an expense\n2. Delete an expense\n3. Update an expense\n4. View all expenses\n5. Show a quick summary\n6. Save and Exit Program")
        option = int(input("Enter your option: "))
        print("=" * 100)

        try:
            if option == 1:
                start_file, expense_id = add(start_file,expense_id)
                print(start_file)
            elif option == 2:
                start_file = delete(start_file)
            elif option == 3:
                start_file = update(start_file)
            elif option == 4:
                print_expenses(start_file)
            elif option == 5:
                expense_summary(start_file)
            elif option == 6:
                save_file(start_file)
                break
        except ValueError:
            print("You have entered an option that isn't allowed")
            program_interface()

#This is the start of the program
program_interface()
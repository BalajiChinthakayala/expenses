import json

def add_expense(expenses, category, amount):
    expenses.append({"category": category, "amount": amount})

def view_expenses(expenses):
    for expense in expenses:
        print(f"Category: {expense['category']}, Amount: {expense['amount']}")

def save_expenses(expenses, filename):
    with open(filename, 'w') as file:
        json.dump(expenses, file)

def load_expenses(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    filename = "expenses.json"
    expenses = load_expenses(filename)

    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Save and exit")
        choice = input("Enter choice: ")

        if choice == '1':
            category = input("Enter category: ")
            amount = float(input("Enter amount: "))
            add_expense(expenses, category, amount)
        elif choice == '2':
            view_expenses(expenses)
        elif choice == '3':
            save_expenses(expenses, filename)
            break
        else:
            print("Invalid choice")

import pandas as pd
import matplotlib.pyplot as plt

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    df = pd.DataFrame([[date, category, amount]], columns=["Date", "Category", "Amount"])
    df.to_csv("expenses.csv", mode="a", header=False, index=False)

def view_summary():
    df = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
    print(df.groupby("Category")["Amount"].sum())

def plot_expenses():
    df = pd.read_csv("expenses.csv", names=["Date", "Category", "Amount"])
    df.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.show()

while True:
    print("1. Add Expense  2. View Summary  3. Plot Expenses  4. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_summary()
    elif choice == "3":
        plot_expenses()
    else:
        break

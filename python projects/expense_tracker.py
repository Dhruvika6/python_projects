import pandas as pd
import os

# Initialize or load expense data
def load_expense_data(file_path='expenses.csv'):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame(columns=["Date", "Category", "Description", "Amount"])

# Save expense data to file
def save_expense_data(df, file_path='expenses.csv'):
    df.to_csv(file_path, index=False)

# Add an expense
def add_expense(df):
    date = input("Enter the date (YYYY-MM-DD): ")
    category = input("Enter the category (e.g., Food, Transport, Utilities): ")
    description = input("Enter a brief description: ")
    amount = float(input("Enter the amount: "))
    
    new_expense = {"Date": date, "Category": category, "Description": description, "Amount": amount}
    df = pd.concat([df, pd.DataFrame([new_expense])], ignore_index=True)
    print("Expense added successfully!")
    return df

# View all expenses
def view_expenses(df):
    print("\nAll Expenses:")
    print(df)

# Generate a report
def generate_report(df):
    if df.empty:
        print("No expenses recorded.")
        return

    print("\nExpense Report:")
    summary = df.groupby("Category")["Amount"].sum().reset_index()
    summary = summary.rename(columns={"Amount": "Total Amount"})
    print(summary)
    print(f"\nTotal Expenses: {df['Amount'].sum()}")

# Main menu
def main():
    file_path = 'expenses.csv'
    expense_data = load_expense_data(file_path)
    
    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            expense_data = add_expense(expense_data)
            save_expense_data(expense_data, file_path)
        elif choice == '2':
            view_expenses(expense_data)
        elif choice == '3':
            generate_report(expense_data)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

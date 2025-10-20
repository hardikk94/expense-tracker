"""
Personal Expense Tracker
A menu-driven application to track daily expenses, categorize them, and manage monthly budgets.
"""

import csv
import os
from datetime import datetime
from typing import List, Dict, Optional


class ExpenseTracker:
    """Main class to manage personal expenses"""
    
    def __init__(self, filename: str = "expenses.csv"):
        self.expenses: List[Dict[str, any]] = []
        self.monthly_budget: Optional[float] = None
        self.filename = filename
        self.load_expenses()
    
    def add_expense(self) -> None:
        """
        Prompt user for expense details and add to the expense list.
        Collects date, category, amount, and description.
        """
        print("\n--- Add New Expense ---")
        
        # Get and validate date
        while True:
            date_str = input("Enter date (YYYY-MM-DD): ").strip()
            try:
                # Validate date format
                datetime.strptime(date_str, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD format.")
        
        # Get category
        category = input("Enter category (e.g., Food, Travel, Entertainment, Bills): ").strip()
        while not category:
            print("Category cannot be empty.")
            category = input("Enter category: ").strip()
        
        # Get and validate amount
        while True:
            try:
                amount_str = input("Enter amount: ").strip()
                amount = float(amount_str)
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        
        # Get description
        description = input("Enter description: ").strip()
        while not description:
            print("Description cannot be empty.")
            description = input("Enter description: ").strip()
        
        # Create expense dictionary
        expense = {
            'date': date_str,
            'category': category,
            'amount': amount,
            'description': description
        }
        
        self.expenses.append(expense)
        print(f"\n✓ Expense added successfully!")
        print(f"  Date: {date_str} | Category: {category} | Amount: ${amount:.2f}")
    
    def view_expenses(self) -> None:
        """
        Display all stored expenses with validation.
        Skip incomplete entries and notify the user.
        """
        print("\n--- View All Expenses ---")
        
        if not self.expenses:
            print("No expenses recorded yet.")
            return
        
        print(f"\nTotal Expenses: {len(self.expenses)}")
        print("-" * 80)
        print(f"{'Date':<12} {'Category':<15} {'Amount':<10} {'Description':<40}")
        print("-" * 80)
        
        valid_count = 0
        invalid_count = 0
        
        for expense in self.expenses:
            # Validate that all required fields are present and non-empty
            if (expense.get('date') and 
                expense.get('category') and 
                expense.get('amount') is not None and 
                expense.get('description')):
                
                date = expense['date']
                category = expense['category']
                amount = expense['amount']
                description = expense['description']
                
                # Truncate description if too long
                if len(description) > 37:
                    description = description[:37] + "..."
                
                print(f"{date:<12} {category:<15} ${amount:<9.2f} {description:<40}")
                valid_count += 1
            else:
                invalid_count += 1
        
        print("-" * 80)
        print(f"Valid entries: {valid_count}")
        
        if invalid_count > 0:
            print(f"⚠ Warning: {invalid_count} incomplete expense(s) were skipped.")
    
    def set_budget(self) -> None:
        """Allow user to set a monthly budget"""
        print("\n--- Set Monthly Budget ---")
        
        while True:
            try:
                budget_str = input("Enter your monthly budget: $").strip()
                budget = float(budget_str)
                if budget <= 0:
                    print("Budget must be greater than 0.")
                    continue
                self.monthly_budget = budget
                print(f"✓ Monthly budget set to ${budget:.2f}")
                break
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
    
    def track_budget(self) -> None:
        """
        Calculate total expenses and compare with monthly budget.
        Display warning if budget exceeded or remaining balance.
        """
        print("\n--- Track Budget ---")
        
        # Calculate total expenses
        total_expenses = sum(
            expense.get('amount', 0) 
            for expense in self.expenses 
            if expense.get('amount') is not None
        )
        
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        if self.monthly_budget is None:
            print("\n⚠ No monthly budget set.")
            response = input("Would you like to set a budget now? (y/n): ").strip().lower()
            if response == 'y':
                self.set_budget()
                # Recalculate with new budget
                if self.monthly_budget:
                    remaining = self.monthly_budget - total_expenses
                    if remaining < 0:
                        print(f"\n⚠ WARNING: You have exceeded your budget by ${abs(remaining):.2f}!")
                    else:
                        print(f"\n✓ You have ${remaining:.2f} left for the month.")
        else:
            print(f"Monthly Budget: ${self.monthly_budget:.2f}")
            remaining = self.monthly_budget - total_expenses
            
            if remaining < 0:
                print(f"\n⚠ WARNING: You have exceeded your budget by ${abs(remaining):.2f}!")
            else:
                percentage_used = (total_expenses / self.monthly_budget) * 100 if self.monthly_budget > 0 else 0
                print(f"\n✓ You have ${remaining:.2f} left for the month.")
                print(f"  Budget used: {percentage_used:.1f}%")
    
    def save_expenses(self) -> None:
        """Save all expenses to a CSV file"""
        try:
            with open(self.filename, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['date', 'category', 'amount', 'description'])
                writer.writeheader()
                writer.writerows(self.expenses)
            
            print(f"\n✓ Expenses saved successfully to '{self.filename}'")
        except Exception as e:
            print(f"\n✗ Error saving expenses: {e}")
    
    def load_expenses(self) -> None:
        """Load expenses from CSV file if it exists"""
        if not os.path.exists(self.filename):
            return
        
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                self.expenses = []
                for row in reader:
                    # Convert amount to float
                    expense = {
                        'date': row['date'],
                        'category': row['category'],
                        'amount': float(row['amount']),
                        'description': row['description']
                    }
                    self.expenses.append(expense)
            
            print(f"✓ Loaded {len(self.expenses)} expense(s) from '{self.filename}'")
        except Exception as e:
            print(f"⚠ Warning: Could not load expenses from file: {e}")
    
    def display_menu(self) -> None:
        """Display the main menu options"""
        print("\n" + "="*50)
        print("       PERSONAL EXPENSE TRACKER")
        print("="*50)
        print("1. Add expense")
        print("2. View expenses")
        print("3. Track budget")
        print("4. Save expenses")
        print("5. Exit")
        print("="*50)
    
    def run(self) -> None:
        """Main program loop with interactive menu"""
        print("\n🎯 Welcome to Personal Expense Tracker!")
        
        while True:
            self.display_menu()
            choice = input("\nEnter your choice (1-5): ").strip()
            
            if choice == '1':
                self.add_expense()
            
            elif choice == '2':
                self.view_expenses()
            
            elif choice == '3':
                self.track_budget()
            
            elif choice == '4':
                self.save_expenses()
            
            elif choice == '5':
                print("\n--- Exiting Program ---")
                self.save_expenses()
                print("\n👋 Thank you for using Personal Expense Tracker!")
                print("Your expenses have been saved. Goodbye!\n")
                break
            
            else:
                print("\n✗ Invalid choice. Please enter a number between 1 and 5.")
            
            # Pause before showing menu again
            input("\nPress Enter to continue...")


def main():
    """Entry point of the application"""
    tracker = ExpenseTracker()
    tracker.run()


if __name__ == "__main__":
    main()


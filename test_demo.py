"""
Demo script to showcase the expense tracker functionality without user interaction
"""

from expense_tracker import ExpenseTracker

def demo():
    print("=" * 70)
    print("  EXPENSE TRACKER - AUTOMATED DEMO")
    print("=" * 70)
    
    # Create tracker instance
    tracker = ExpenseTracker("demo_expenses.csv")
    
    print("\n📝 Step 1: Adding sample expenses programmatically...")
    
    # Add sample expenses directly
    sample_expenses = [
        {
            'date': '2024-10-15',
            'category': 'Food',
            'amount': 25.50,
            'description': 'Breakfast at cafe'
        },
        {
            'date': '2024-10-16',
            'category': 'Travel',
            'amount': 45.00,
            'description': 'Uber to airport'
        },
        {
            'date': '2024-10-17',
            'category': 'Entertainment',
            'amount': 30.00,
            'description': 'Concert tickets'
        },
        {
            'date': '2024-10-18',
            'category': 'Bills',
            'amount': 120.00,
            'description': 'Internet bill'
        },
        {
            'date': '2024-10-19',
            'category': 'Food',
            'amount': 18.75,
            'description': 'Dinner at restaurant'
        }
    ]
    
    tracker.expenses.extend(sample_expenses)
    print(f"✓ Added {len(sample_expenses)} sample expenses")
    
    # View expenses
    print("\n" + "=" * 70)
    print("📊 Step 2: Viewing all expenses")
    print("=" * 70)
    tracker.view_expenses()
    
    # Set budget
    print("\n" + "=" * 70)
    print("💰 Step 3: Setting monthly budget to $500.00")
    print("=" * 70)
    tracker.monthly_budget = 500.00
    print("✓ Budget set successfully")
    
    # Track budget
    print("\n" + "=" * 70)
    print("📈 Step 4: Tracking budget")
    print("=" * 70)
    tracker.track_budget()
    
    # Save expenses
    print("\n" + "=" * 70)
    print("💾 Step 5: Saving expenses to file")
    print("=" * 70)
    tracker.save_expenses()
    
    # Calculate some statistics
    print("\n" + "=" * 70)
    print("📊 EXPENSE SUMMARY")
    print("=" * 70)
    
    total = sum(e['amount'] for e in tracker.expenses)
    categories = {}
    for expense in tracker.expenses:
        cat = expense['category']
        categories[cat] = categories.get(cat, 0) + expense['amount']
    
    print(f"\nTotal Expenses: ${total:.2f}")
    print(f"Number of Transactions: {len(tracker.expenses)}")
    print(f"Average Expense: ${total/len(tracker.expenses):.2f}")
    
    print("\n📋 Spending by Category:")
    print("-" * 40)
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        percentage = (amount / total) * 100
        print(f"  {category:<20} ${amount:>8.2f}  ({percentage:>5.1f}%)")
    
    print("\n" + "=" * 70)
    print("✅ DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\n💡 To use the interactive version, run:")
    print("   python3 expense_tracker.py")
    print("\n")

if __name__ == "__main__":
    demo()

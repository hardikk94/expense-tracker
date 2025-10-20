# Personal Expense Tracker 💰

A command-line personal expense tracker application that helps you manage daily expenses, categorize spending, and track against monthly budgets. All expense data is automatically saved to a CSV file for future reference.

## Features ✨

- **Add Expenses**: Log expenses with date, category, amount, and description
- **View Expenses**: Display all recorded expenses in a formatted table
- **Budget Tracking**: Set monthly budgets and track spending against them
- **Data Persistence**: Automatically save and load expenses from CSV file
- **Input Validation**: Robust validation for dates, amounts, and required fields
- **Interactive Menu**: Easy-to-use menu-driven interface

## Requirements 📋

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation 🚀

1. Clone or download this repository
2. Navigate to the project directory:
   ```bash
   cd IITK
   ```

## Usage 🎯

### Running the Application

Simply run the Python script:

```bash
python3 expense_tracker.py
```

### Menu Options

When you run the application, you'll see an interactive menu with the following options:

```
1. Add expense       - Record a new expense
2. View expenses     - Display all stored expenses
3. Track budget      - View total spending and budget status
4. Save expenses     - Manually save expenses to CSV file
5. Exit              - Save and exit the program
```

### Adding an Expense

When you select option 1, you'll be prompted to enter:

- **Date**: In YYYY-MM-DD format (e.g., 2024-09-18)
- **Category**: Type of expense (e.g., Food, Travel, Entertainment, Bills)
- **Amount**: Numeric value (must be greater than 0)
- **Description**: Brief description of the expense

**Example:**
```
Enter date (YYYY-MM-DD): 2024-09-18
Enter category: Food
Enter amount: 15.50
Enter description: Lunch with friends
```

### Viewing Expenses

Option 2 displays all expenses in a formatted table:

```
Date         Category        Amount     Description
------------------------------------------------------------------------
2024-09-18   Food           $15.50     Lunch with friends
2024-09-19   Travel         $50.00     Taxi to office
```

### Tracking Budget

Option 3 allows you to:
- Set a monthly budget (if not already set)
- View total expenses
- See remaining budget or overspending warning

**Output examples:**
- If within budget: `✓ You have $150.00 left for the month.`
- If over budget: `⚠ WARNING: You have exceeded your budget by $50.00!`

### Data Persistence

- Expenses are automatically saved to `expenses.csv` when you exit (option 5)
- You can also manually save using option 4
- When you restart the application, previous expenses are automatically loaded

## File Structure 📁

```
IITK/
├── expense_tracker.py    # Main application file
├── expenses.csv          # Auto-generated expense data file
└── README.md            # This file
```

## CSV File Format 📄

The `expenses.csv` file stores expenses with the following columns:

```csv
date,category,amount,description
2024-09-18,Food,15.50,Lunch with friends
2024-09-19,Travel,50.00,Taxi to office
```

## Input Validation ✅

The application includes comprehensive input validation:

- **Date**: Must be in YYYY-MM-DD format
- **Category**: Cannot be empty
- **Amount**: Must be a positive number
- **Description**: Cannot be empty
- **Incomplete entries**: Automatically skipped when viewing expenses

## Example Session 💡

```
🎯 Welcome to Personal Expense Tracker!
✓ Loaded 2 expense(s) from 'expenses.csv'

==================================================
       PERSONAL EXPENSE TRACKER
==================================================
1. Add expense
2. View expenses
3. Track budget
4. Save expenses
5. Exit
==================================================

Enter your choice (1-5): 1

--- Add New Expense ---
Enter date (YYYY-MM-DD): 2024-10-20
Enter category (e.g., Food, Travel, Entertainment, Bills): Food
Enter amount: 25.00
Enter description: Dinner at restaurant

✓ Expense added successfully!
  Date: 2024-10-20 | Category: Food | Amount: $25.00

Press Enter to continue...
```

## Tips 💡

1. **Regular Saving**: Although expenses auto-save on exit, use option 4 to save manually during long sessions
2. **Budget Tracking**: Set your monthly budget early to track spending throughout the month
3. **Consistent Categories**: Use consistent category names (e.g., always "Food" not "food" or "Meals")
4. **Date Format**: Always use YYYY-MM-DD format for proper date sorting
5. **Backup**: Keep backups of your `expenses.csv` file periodically

## Troubleshooting 🔧

**Problem**: "Could not load expenses from file"
- **Solution**: The CSV file might be corrupted. Delete `expenses.csv` and start fresh.

**Problem**: "Invalid date format"
- **Solution**: Ensure you're using YYYY-MM-DD format (e.g., 2024-10-20, not 20/10/2024)

**Problem**: "Invalid amount"
- **Solution**: Enter only numeric values without currency symbols (e.g., 15.50, not $15.50)

## Future Enhancements 🚀

Potential features for future versions:
- Monthly/weekly expense summaries
- Category-wise spending analysis
- Export to PDF or Excel
- Multiple budget categories
- Expense filtering by date range
- Graphical visualization of spending patterns

## License 📝

This project is open source and available for educational purposes.

## Author ✍️

Created as part of the IITK project requirements for personal expense management.

---

**Happy Expense Tracking!** 🎉


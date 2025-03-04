# Expense-tracker-cli

This Python script is a simple command-line expense tracker that allows you to record, manage, and summarize your expenses. It uses a CSV file to store your expense data, enabling you to save and load your records between sessions.

## Features

-   **Add Expenses:** Easily add new expenses with descriptions and amounts.
-   **Delete Expenses:** Remove unwanted expenses by their unique ID.
-   **Update Expenses:** Modify the description or amount of existing expenses.
-   **View Expenses:** Display a formatted list of all recorded expenses.
-   **Expense Summary:** Get a quick overview of your total expenses.
-   **Save and Load:** Persist your expense data to a CSV file (`expenses_save.csv`).

## Getting Started

### Prerequisites

-   Python 3.x installed on your system.

### Usage

1.  **Clone the Repository:**
    ```bash
    git clone [repository_url]
    cd [repository_directory]
    ```

2.  **Run the Script:**
    ```bash
    python your_script_name.py
    ```
    (Replace `your_script_name.py` with the actual name of your Python file.)

3.  **Follow the Menu:**
    -   The script will display a menu with options to add, delete, update, view, summarize, and save expenses.
    -   Enter the number corresponding to your desired action and follow the prompts.

### File Structure

-   `expenses_save.csv`: Stores your expense records. This file will be created or updated when you save your expenses.
-   `your_script_name.py`: The Python script containing the expense tracker logic.

### Example Usage
====================================================================================================
Welcome to your Expense Tracker
What would you like to do?

Add an expense
Delete an expense
Update an expense
View all expenses
Show a quick summary
Save and Exit Program 
Enter your option: 1 
==================================================================================================== 
Enter the amount of your expense: 25.50 
What did you spend this money on: Lunch 
You've added a new expense [{'id': 1, 'date': '2024-10-27', 'description': 'Lunch', 'amount': 25.5}] 
... 
Enter your option: 4 
==================================================================================================== 
Here are your expenses so far 
ID Date Description Amount 
1 2024-10-27 Lunch $25.5 
Done 
... 
Enter your option: 6 
==================================================================================================== 
Saving your records
... 
Your expenses have been saved to expenses_save.csv

##Contributing
Feel free to contribute to this project by submitting pull requests or opening issues.

Link to roadmap.sh project - https://roadmap.sh/projects/expense-tracker

# Finance Tracker

A command-line interface (CLI) application for managing personal finances, built with Python. The application allows users to track income and expenses, set and monitor budgets, and view financial summaries.

## How It Works

### Core Features
- **Transaction Management**: Add and view income and expense transactions with categories and descriptions
- **Budget Tracking**: Set monthly budgets for different categories and monitor spending against these budgets
- **Financial Analytics**: View a summary of total income, expenses, and balance
- **Interactive CLI**: User-friendly menu-based interface using questionary for selections

### Architecture
The application is organized into three main modules:
1. **Transactions Module**: Handles adding and listing transactions with date, type (income/expense), amount, category, and description
2. **Budgets Module**: Allows setting monthly budgets by category and compares actual spending against budgets
3. **Analytics Module**: Provides financial summaries showing total income, expenses, and balance

### Data Storage
- Transactions and budgets are stored in plain text files in the `database/` directory
- Amounts are stored as integers (in paisa) to avoid floating-point errors
- Transaction format: `date,type,amount_in_paisa,category,description`
- Budget format: `category,amount_in_paisa`

### Tech Stack
- Python 3.13+
- Questionary: For interactive CLI menus
- Rich: For formatted tables and UI elements
- Plain text files: For data storage

### Usage Flow
1. User runs `main.py` to start the CLI
2. Application presents a menu with options to add transactions, view transactions, set budgets, view budgets, or see financial summaries
3. Based on user selection, appropriate modules handle the requested functionality
4. Data is persisted to text files in the database directory
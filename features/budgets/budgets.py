from datetime import datetime
import questionary
from rich.console import Console
from rich.progress import ProgressBar
from rich.table import Table

console = Console()

def set_budget():
    """Sets a monthly budget for a specific category."""
    category = questionary.select(
        "Select a category to budget:",
        choices=["Food", "Transport", "Shopping", "Bills", "Entertainment", "Health", "Other"],
    ).ask()

    amount = questionary.text(f"Enter the monthly budget for {category}:").ask()

    # Validate amount
    try:
        budget_paisa = int(float(amount) * 100)
    except ValueError:
        console.print("Invalid amount. Please enter a number.", style="bold red")
        return

    # Store budget
    with open("database/budgets.txt", "a") as f:
        f.write(f"{category},{budget_paisa}\n")

    console.print(f"Budget for {category} set to ₹{amount} successfully!", style="bold green")


def view_budgets():
    """Displays the budget vs actual spending for each category."""
    try:
        with open("database/budgets.txt", "r") as f:
            budgets = f.readlines()
    except FileNotFoundError:
        console.print("No budgets found. Please set a budget first.", style="bold red")
        return

    try:
        with open("database/transactions.txt", "r") as f:
            transactions = f.readlines()
    except FileNotFoundError:
        transactions = []

    # Get current month
    current_month = datetime.now().strftime("%Y-%m")

    # Calculate spending per category for the current month
    spending = {}
    for transaction in transactions:
        date, transaction_type, amount_paisa, category, _ = transaction.strip().split(",")
        if date.startswith(current_month) and transaction_type == "Expense":
            if category not in spending:
                spending[category] = 0
            spending[category] += int(amount_paisa)

    table = Table(title="Budget vs Spending")
    table.add_column("Category", justify="left", style="cyan")
    table.add_column("Budget", justify="right", style="magenta")
    table.add_column("Spent", justify="right", style="red")
    table.add_column("Remaining", justify="right", style="green")
    table.add_column("Utilization", justify="center", no_wrap=True)

    total_budget = 0
    total_spent = 0

    for budget_line in budgets:
        category, budget_paisa = budget_line.strip().split(",")
        budget = int(budget_paisa)
        spent = spending.get(category, 0)
        remaining = budget - spent
        utilization = (spent / budget) * 100 if budget > 0 else 0

        total_budget += budget
        total_spent += spent

        # Determine status and color
        if utilization > 100:
            status = "Over"
            color = "bold red"
        elif utilization >= 70:
            status = "Warning"
            color = "bold yellow"
        else:
            status = "OK"
            color = "bold green"

        # Create progress bar
        progress = ProgressBar(total=100, completed=utilization, width=20)

        table.add_row(
            category,
            f"₹{budget / 100:.2f}",
            f"₹{spent / 100:.2f}",
            f"₹{remaining / 100:.2f}",
            f"[{color}]{utilization:.2f}%[/] ({status}) {progress}",
        )
    
    total_remaining = total_budget - total_spent
    total_utilization = (total_spent / total_budget) * 100 if total_budget > 0 else 0

    table.add_section()
    table.add_row("Total", f"₹{total_budget / 100:.2f}", f"₹{total_spent / 100:.2f}", f"₹{total_remaining / 100:.2f}", f"{total_utilization:.2f}%")
    console.print(table)


from datetime import datetime
import questionary
import rich
from rich.console import Console
from rich.table import Table


console = Console()

def add_transaction():
    """Adds a new transaction to the database."""
    transaction_type = questionary.select(
        "Select transaction type:", choices=["Expense", "Income"]
    ).ask()

    amount = questionary.text("Enter the amount:").ask()
    category = questionary.select(
        "Select a category:",
        choices=[
            "Food",
            "Transport",
            "Shopping",
            "Bills",
            "Entertainment",
            "Health",
            "Other",
        ]
        if transaction_type == "Expense"
        else ["Salary", "Freelance", "Business", "Investment", "Gift", "Other"],
    ).ask()

    description = questionary.text("Enter a description:").ask()

    # Validate amount
    try:
        amount_paisa = int(float(amount) * 100)
    except ValueError:
        console.print("Invalid amount. Please enter a number.", style="bold red")
        return

    # Get current date
    date = datetime.now().strftime("%Y-%m-%d")

    # Store transaction
    with open("database/transactions.txt", "a") as f:
        f.write(
            f"{date},{transaction_type},{amount_paisa},{category},{description}\n"
        )

    console.print("Transaction added successfully!", style="bold green")


def list_transactions():
    """Lists all transactions in a table."""
    try:
        with open("database/transactions.txt", "r") as f:
            transactions = f.readlines()
    except FileNotFoundError:
        console.print("No transactions found.", style="bold red")
        return

    table = Table(title="All Transactions")
    table.add_column("Date", justify="center", style="cyan")
    table.add_column("Type", justify="center", style="magenta")
    table.add_column("Amount", justify="right", style="green")
    table.add_column("Category", justify="center", style="yellow")
    table.add_column("Description", justify="left", style="white")

    for transaction in transactions:
        date, transaction_type, amount_paisa, category, description = (
            transaction.strip().split(",")
        )
        amount = int(amount_paisa) / 100
        style = "red" if transaction_type == "Expense" else "green"
        table.add_row(
            date,
            transaction_type,
            f"₹{amount:.2f}",
            category,
            description,
            style=style,
        )

    console.print(table)

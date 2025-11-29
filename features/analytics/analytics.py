from rich.console import Console
from rich.table import Table

console = Console()

def view_summary():
    """Displays a summary of all transactions."""
    try:
        with open("database/transactions.txt", "r") as f:
            transactions = f.readlines()
    except FileNotFoundError:
        console.print("No transactions found.", style="bold red")
        return

    total_income = 0
    total_expense = 0

    for transaction in transactions:
        _, transaction_type, amount_paisa, _, _ = transaction.strip().split(",")
        amount = int(amount_paisa) / 100
        if transaction_type == "Income":
            total_income += amount
        else:
            total_expense += amount

    balance = total_income - total_expense

    table = Table(title="Financial Summary")
    table.add_column("Metric", justify="right", style="cyan", no_wrap=True)
    table.add_column("Amount", justify="right", style="magenta")

    table.add_row("Total Income", f"[green]₹{total_income:.2f}[/green]")
    table.add_row("Total Expense", f"[red]₹{total_expense:.2f}[/red]")
    table.add_row("Balance", f"[bold green]₹{balance:.2f}[/bold green]" if balance >= 0 else f"[bold red]₹{balance:.2f}[/bold red]")

    console.print(table)

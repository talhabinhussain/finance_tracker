import questionary
from rich.console import Console
from features.transactions.transactions import add_transaction, list_transactions
from features.analytics.analytics import view_summary
from features.budgets.budgets import set_budget, view_budgets

console = Console()


def main():
    console.print("Welcome to your Finance Tracker!", style="bold green")
    while True:
        action = questionary.select(
            "What would you like to do?",
            choices=[
                "Add a new transaction",
                "List all transactions",
                "View summary",
                "Set a new budget",
                "View budgets",
                "Exit",
            ],
        ).ask()

        if action == "Add a new transaction":
            add_transaction()
        elif action == "List all transactions":
            list_transactions()
        elif action == "View summary":
            view_summary()
        elif action == "Set a new budget":
            set_budget()
        elif action == "View budgets":
            view_budgets()
        elif action == "Exit":
            break

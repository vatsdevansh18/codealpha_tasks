"""A menu-driven stock portfolio tracker using demonstration stock prices."""

from datetime import datetime
from pathlib import Path


STOCK_PRICES = {"AAPL": 180.00, "TSLA": 250.00, "GOOGL": 175.00, "MSFT": 420.00, "AMZN": 190.00}
SUMMARY_FILE = Path(__file__).with_name("portfolio_summary.txt")


def calculate_total(portfolio):
    """Calculate the current total investment value."""
    return sum(STOCK_PRICES[symbol] * shares for symbol, shares in portfolio.items())


def show_prices():
    """Display the hardcoded demonstration prices in a clear table."""
    print("\nAvailable stocks (sample prices)")
    print("-" * 32)
    for symbol, price in STOCK_PRICES.items():
        print(f"{symbol:<8} ${price:>10.2f}")


def get_positive_quantity(symbol, action):
    """Read and validate a positive whole number of shares."""
    while True:
        try:
            quantity = int(input(f"Shares to {action} for {symbol}: "))
            if quantity > 0:
                return quantity
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Please enter a whole number, such as 5.")


def show_portfolio(portfolio):
    """Print a portfolio breakdown, allocation percentage, and total investment."""
    if not portfolio:
        print("\nYour portfolio is empty.")
        return 0

    total = calculate_total(portfolio)
    print("\n" + "=" * 66)
    print("                         PORTFOLIO SUMMARY")
    print("=" * 66)
    print(f"{'Stock':<10}{'Shares':>10}{'Price':>14}{'Value':>16}{'Allocation':>14}")
    print("-" * 66)
    for symbol, shares in portfolio.items():
        value = STOCK_PRICES[symbol] * shares
        allocation = (value / total) * 100
        price_text = f"${STOCK_PRICES[symbol]:,.2f}"
        value_text = f"${value:,.2f}"
        print(f"{symbol:<10}{shares:>10}{price_text:>14}{value_text:>16}{allocation:>13.1f}%")
    print("=" * 66)
    print(f"Total investment value: ${total:,.2f}")
    return total


def save_portfolio(portfolio):
    """Save a detailed, readable investment report beside this program."""
    total = calculate_total(portfolio)
    timestamp = datetime.now().strftime("%d %B %Y, %I:%M %p")
    lines = ["STOCK PORTFOLIO REPORT", f"Generated: {timestamp}", "=" * 48]
    for symbol, shares in portfolio.items():
        price = STOCK_PRICES[symbol]
        value = price * shares
        lines.append(f"{symbol}: {shares} share(s) x ${price:.2f} = ${value:.2f}")
    lines.extend(["=" * 48, f"TOTAL INVESTMENT VALUE: ${total:.2f}"])
    SUMMARY_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report saved to: {SUMMARY_FILE}")


def main():
    """Run the portfolio tracker menu."""
    portfolio = {}
    print("\nWelcome to the Stock Portfolio Tracker")
    print("Note: Prices are hardcoded samples for this educational project.")

    while True:
        print("\n1. View available stocks\n2. Buy shares\n3. Sell shares\n4. View portfolio\n5. Save report\n6. Exit")
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            show_prices()
        elif choice == "2":
            show_prices()
            symbol = input("Enter a stock symbol: ").upper().strip()
            if symbol not in STOCK_PRICES:
                print("That symbol is not in the available stock list.")
                continue
            portfolio[symbol] = portfolio.get(symbol, 0) + get_positive_quantity(symbol, "buy")
            print(f"Purchase recorded. Current investment: ${calculate_total(portfolio):,.2f}")
        elif choice == "3":
            if not portfolio:
                print("Your portfolio is empty. Buy shares before selling.")
                continue
            show_portfolio(portfolio)
            symbol = input("Enter the symbol to sell: ").upper().strip()
            if symbol not in portfolio:
                print("You do not currently own that stock.")
                continue
            quantity = get_positive_quantity(symbol, "sell")
            if quantity > portfolio[symbol]:
                print(f"You only own {portfolio[symbol]} share(s) of {symbol}.")
                continue
            portfolio[symbol] -= quantity
            if portfolio[symbol] == 0:
                del portfolio[symbol]
            print(f"Sale recorded. Current investment: ${calculate_total(portfolio):,.2f}")
        elif choice == "4":
            show_portfolio(portfolio)
        elif choice == "5":
            if portfolio:
                save_portfolio(portfolio)
            else:
                print("Add at least one stock before saving a report.")
        elif choice == "6":
            if portfolio:
                print(f"Final investment value: ${calculate_total(portfolio):,.2f}")
            print("Thanks for using the portfolio tracker.")
            break
        else:
            print("Invalid option. Please choose a number from 1 to 6.")


if __name__ == "__main__":
    main()

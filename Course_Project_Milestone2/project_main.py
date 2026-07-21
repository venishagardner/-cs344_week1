# Smart Paycheck Budget Allocator
# This program helps the user divide monthly income between bills,
# savings, a rainy-day fund, and a splurge fund.


def get_income():
    """Collect paycheck information and calculate monthly income."""

    paycheck_amount = float(
        input("Enter your take-home amount for one paycheck: $")
    )

    paycheck_count = int(
        input("How many paychecks do you receive each month? ")
    )

    monthly_income = paycheck_amount * paycheck_count

    return monthly_income, paycheck_count


def get_bills():
    """Collect recurring bills and calculate the total bill amount."""

    bills = []
    total_bills = 0

    print("\nEnter your recurring monthly bills.")
    print("Type done when you are finished.")

    while True:
        bill_name = input("\nEnter the bill name or type done: ")

        if bill_name.lower() == "done":
            break

        bill_amount = float(
            input(f"Enter the monthly amount for {bill_name}: $")
        )

        bills.append((bill_name, bill_amount))
        total_bills += bill_amount

    return bills, total_bills


def calculate_budget(monthly_income, paycheck_count, total_bills):
    """Calculate savings, rainy-day funds, splurge funds, and balance."""

    savings = 50 * paycheck_count
    rainy_day_fund = 200

    money_after_required_expenses = (
        monthly_income - total_bills - savings - rainy_day_fund
    )

    if money_after_required_expenses < 0:
        splurge_fund = 0
        remaining_balance = money_after_required_expenses

    elif money_after_required_expenses > 1200:
        splurge_fund = 1200
        remaining_balance = money_after_required_expenses - splurge_fund

    else:
        splurge_fund = money_after_required_expenses
        remaining_balance = 0

    return savings, rainy_day_fund, splurge_fund, remaining_balance


def display_summary(
    monthly_income,
    bills,
    total_bills,
    savings,
    rainy_day_fund,
    splurge_fund,
    remaining_balance
):
    """Display the user's final monthly budget summary."""

    print("\nSMART PAYCHECK BUDGET SUMMARY")
    print("--------------------------------")

    print(f"Monthly take-home income: ${monthly_income:.2f}")

    print("\nRecurring bills:")

    for bill_name, bill_amount in bills:
        print(f"{bill_name}: ${bill_amount:.2f}")

    print(f"\nTotal recurring bills: ${total_bills:.2f}")
    print(f"Suggested savings: ${savings:.2f}")
    print(f"Suggested rainy-day fund: ${rainy_day_fund:.2f}")
    print(f"Suggested splurge fund: ${splurge_fund:.2f}")
    print(f"Remaining balance: ${remaining_balance:.2f}")

    if remaining_balance < 0:
        print("\nWarning: Your income does not cover all planned expenses.")

    elif splurge_fund == 1200:
        print("\nYour splurge fund reached the maximum limit of $1,200.")

    else:
        print("\nYour monthly income covers the suggested budget.")


def main():
    """Coordinate the overall flow of the program."""

    print("Welcome to the Smart Paycheck Budget Allocator!")

    monthly_income, paycheck_count = get_income()

    bills, total_bills = get_bills()

    savings, rainy_day_fund, splurge_fund, remaining_balance = (
        calculate_budget(
            monthly_income,
            paycheck_count,
            total_bills
        )
    )

    display_summary(
        monthly_income,
        bills,
        total_bills,
        savings,
        rainy_day_fund,
        splurge_fund,
        remaining_balance
    )


main()

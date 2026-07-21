# This function displays the completed budget summary.


def display_summary(
    monthly_income,
    bills,
    total_bills,
    savings,
    rainy_day_fund,
    splurge_fund,
    remaining_balance,
    budget_status
):
    print("\nSMART PAYCHECK BUDGET SUMMARY")
    print("--------------------------------")

    print(f"Monthly take-home income: ${monthly_income:.2f}")

    print("\nRecurring bills:")

    if len(bills) == 0:
        print("No recurring bills were entered.")

    else:
        for bill_name, bill_amount in bills:
            print(f"{bill_name}: ${bill_amount:.2f}")

    print(f"\nTotal recurring bills: ${total_bills:.2f}")
    print(f"Suggested savings: ${savings:.2f}")
    print(f"Suggested rainy-day fund: ${rainy_day_fund:.2f}")
    print(f"Suggested splurge fund: ${splurge_fund:.2f}")
    print(f"Remaining balance: ${remaining_balance:.2f}")

    print(f"\nBudget status: {budget_status}")

# This function collects recurring monthly bills
# and adds them together.


def get_bills():
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

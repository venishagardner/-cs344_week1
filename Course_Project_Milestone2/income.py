 # This function collects paycheck information
# and calculates the user's monthly income.


def get_income():
    paycheck_amount = float(
        input("Enter your take-home amount for one paycheck: $")
    )

    paycheck_count = int(
        input("How many paychecks do you receive each month? ")
    )

    monthly_income = paycheck_amount * paycheck_count

    return monthly_income, paycheck_count

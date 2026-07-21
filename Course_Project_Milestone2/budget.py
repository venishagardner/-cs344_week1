# This function calculates the suggested savings,
# rainy-day fund, splurge fund, and remaining balance.


def calculate_budget(monthly_income, paycheck_count, total_bills):
    savings = 50 * paycheck_count
    rainy_day_fund = 200

    available_money = (
        monthly_income
        - total_bills
        - savings
        - rainy_day_fund
    )

    if available_money < 0:
        splurge_fund = 0
        remaining_balance = available_money
        budget_status = "Your income does not cover all planned expenses."

    elif available_money > 1200:
        splurge_fund = 1200
        remaining_balance = available_money - splurge_fund
        budget_status = "Your splurge fund reached the $1,200 limit."

    else:
        splurge_fund = available_money
        remaining_balance = 0
        budget_status = "Your income covers the suggested budget."

    return (
        savings,
        rainy_day_fund,
        splurge_fund,
        remaining_balance,
        budget_status
    )

import frappe
from frappe.website.website_generator import WebsiteGenerator
from loan_calculator.loan_calculator.doctype.calculate_interest.interest_utils import (
    calculate_monthly_interest,
    calculate_monthly_interest_compounded,
    calculate_daily_interest,
    calculate_daily_interest_compounded,
)

class CalculateInterest(WebsiteGenerator):
    def get_context(self, context):
        # Pass existing values to the template for pre-filling the form
        context.balance = self.balance
        context.annual_rate = self.annual_rate
        context.periods = self.periods or 1
        context.calculation_method = self.calculation_method or "monthly"
        
        return context

@frappe.whitelist()
def calculate_interest(balance, annual_rate, periods=1, calculation_method="monthly"):
    balance = float(balance)
    annual_rate = float(annual_rate)

    # Convert periods to float, then cast to an integer
    try:
        periods = int(periods)
    except ValueError:
        frappe.throw(f"Invalid value for periods: {periods}. It should be an integer.")

    if calculation_method == "monthly":
        interest = calculate_monthly_interest(balance, annual_rate, periods)
    elif calculation_method == "monthly_compounded":
        interest = calculate_monthly_interest_compounded(balance, annual_rate, periods)
    elif calculation_method == "daily":
        interest = calculate_daily_interest(balance, annual_rate, periods)
    elif calculation_method == "daily_compounded":
        interest = calculate_daily_interest_compounded(balance, annual_rate, periods)
    else:
        frappe.throw(f"Unsupported calculation method: {calculation_method}")
    
    return {"message": interest}


import frappe
from frappe.website.website_generator import WebsiteGenerator
from loan_calculator.loan_calculator.doctype.calculate_interest.interest_utils import (
    calculate_monthly_interest,
    calculate_monthly_interest_compounded,
    calculate_daily_interest,
    calculate_daily_interest_compounded,
    get_interest_rate_to_use,
)

class CalculateInterest(WebsiteGenerator):
    def before_save(self):
        if not self.balance or not self.annual_rate:
            frappe.throw("Balance and Annual Rate are required to calculate interest.")
        
        periods = self.periods or 1
        calculation_method = self.calculation_method or "monthly"
        
        if calculation_method == "monthly":
            self.calculated_interest = calculate_monthly_interest(self.balance, self.annual_rate, periods)
        elif calculation_method == "monthly_compounded":
            self.calculated_interest = calculate_monthly_interest_compounded(self.balance, self.annual_rate, periods)
        elif calculation_method == "daily":
            self.calculated_interest = calculate_daily_interest(self.balance, self.annual_rate, periods)
        elif calculation_method == "daily_compounded":
            self.calculated_interest = calculate_daily_interest_compounded(self.balance, self.annual_rate, periods)
        else:
            frappe.throw(f"Unsupported calculation method: {calculation_method}")
    
# The function is now outside of the class and is a standalone function
@frappe.whitelist()
def calculate_interest(balance, annual_rate, periods=1, calculation_method="monthly"):
    balance = float(balance)
    annual_rate = float(annual_rate)
    periods = int(periods)

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
